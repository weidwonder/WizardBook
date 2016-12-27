#include <iostream>
#include <iomanip>
#include <stdexcept>
#include <vector>

#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/gpu/gpu.hpp>
#include <opencv2/video/video.hpp>
#include <opencv2/calib3d/calib3d.hpp>

#include "utility.hpp"

using namespace std;
using namespace cv;
using namespace cv::gpu;

enum Method
{
    MOG,
    METHOD_MAX
};

const char* method_str[] =
{
    "MOG"
};

class App : public BaseApp
{
public:
    App();

protected:
    void runAppLogic();
    void processAppKey(int key);
    void printAppHelp();
    bool parseAppCmdArgs(int& i, int argc, const char* argv[]);

private:
    void displayState(Mat& outImg, double proc_fps, double total_fps);

    Method method_;
    bool useGpu_;
    int curSource_;
    bool fullscreen_;
    bool reinitialize_;
};

App::App()
{
    method_ = MOG;
    useGpu_ = true;
    curSource_ = 0;
    fullscreen_ = false;
    reinitialize_ = true;
}

void App::runAppLogic()
{
    if (sources_.empty())
    {
        cout << "Using default frames source... \n" << endl;
        sources_.push_back(FrameSource::video("data/background_subtraction.avi"));
    }

    BackgroundSubtractorMOG mog_cpu;
    MOG_GPU mog_gpu;

    Mat frame, fgmask, filterBuf, outImg;
    GpuMat d_frame, d_fgmask;

    const string wndName = "Background Subtraction Demo";

    if (fullscreen_)
    {
        namedWindow(wndName, WINDOW_NORMAL);
        setWindowProperty(wndName, WND_PROP_FULLSCREEN, CV_WINDOW_FULLSCREEN);
        setWindowProperty(wndName, WND_PROP_ASPECT_RATIO, CV_WINDOW_FREERATIO);
    }

    while (isActive())
    {
        const int64 total_start = getTickCount();

        if (reinitialize_)
        {
            mog_cpu = BackgroundSubtractorMOG();
            mog_gpu.release();

            sources_[curSource_]->reset();

            reinitialize_ = false;
        }

        sources_[curSource_]->next(frame);

        if (useGpu_)
            d_frame.upload(frame);

        const int64 proc_start = getTickCount();

        switch (method_)
        {
        case MOG:
        {
            if (useGpu_)
                mog_gpu(d_frame, d_fgmask, 0.01f);
            else
                mog_cpu(frame, fgmask, 0.01);
            break;
        }

        default:
            ;
        }

        const double proc_fps = getTickFrequency() / (getTickCount() - proc_start);

        if (useGpu_)
            d_fgmask.download(fgmask);

        filterSpeckles(fgmask, 0, 100, 1, filterBuf);

        outImg.create(frame.rows, frame.cols * 2, CV_8UC3);

        Mat left = outImg(Rect(0, 0, frame.cols, frame.rows));
        Mat right = outImg(Rect(frame.cols, 0, frame.cols, frame.rows));

        frame.copyTo(left);
        add(left, cv::Scalar(100, 100, 0), left, fgmask);

        right.setTo(0);
        frame.copyTo(right, fgmask);

        const double total_fps = getTickFrequency() / (getTickCount() - total_start);

        displayState(outImg, proc_fps, total_fps);

        imshow(wndName, outImg);

        wait(30);
    }
}

void App::displayState(Mat& outImg, double proc_fps, double total_fps)
{
    const Scalar fontColorRed = CV_RGB(255, 0, 0);

    ostringstream txt;
    int i = 0;

    txt.str(""); txt << "Source size: " << outImg.cols / 2 << 'x' << outImg.rows;
    printText(outImg, txt.str(), i++);

    txt.str(""); txt << "Method: " << method_str[method_] << (useGpu_ ? " CUDA" : " CPU");
    printText(outImg, txt.str(), i++);

    txt.str(""); txt << "FPS (BG only): " << fixed << setprecision(1) << proc_fps;
    printText(outImg, txt.str(), i++);

    txt.str(""); txt << "FPS (Total): " << fixed << setprecision(1) << total_fps;
    printText(outImg, txt.str(), i++);

    printText(outImg, "Space - switch CUDA / CPU mode", i++, fontColorRed);

    if (sources_.size() > 1)
        printText(outImg, "N - switch source", i++, fontColorRed);
}

void App::processAppKey(int key)
{
    switch (toupper(key & 0xff))
    {
    case 32 /*space*/:
        {
            useGpu_ = !useGpu_;
            reinitialize_ = true;
            cout << "Switch mode to " << (useGpu_ ? "CUDA" : "CPU") << endl;
        }
        break;

    case 'N':
        if (sources_.size() > 1)
        {
            curSource_ = (curSource_ + 1) % sources_.size();
            reinitialize_ = true;
            cout << "Switch source to " << curSource_ << endl;
        }
        break;
    }
}

void App::printAppHelp()
{
    cout << "This sample demonstrates different Background Subtraction algorithms \n" << endl;

    cout << "Usage: demo_background_subtraction [options] \n" << endl;

    cout << "Launch Options: \n"
         << "  --fullscreen \n"
         << "       Launch in fullscreen mode \n" << endl;
}

bool App::parseAppCmdArgs(int& i, int, const char* argv[])
{
    string arg(argv[i]);

    if (arg == "--fullscreen")
    {
        fullscreen_ = true;
        return true;
    }

    return false;
}

RUN_APP(App)
