#include<windows.h>
//声明WndProc()函数
LRESULT CALLBACK WndProc(
	HWND hwnd, UINT message,
	WPARAM wParam,
	LPARAM lParam);
//编写WinMain()主函数
int APIENTRY WinMain(HINSTANCE hInstance,
	HINSTANCE hPrevInstance,
	LPSTR lpCmdLine,
	int nCmdShow)
{
	WNDCLASS wndclass;									//定义窗口类结构变量
	HWND hwnd; 											//定义窗口句柄
	MSG msg;											//定义消息结构变量
	char lpszClassName[] = "自己创建的窗口";

	//设计窗口类型
	wndclass.style = CS_HREDRAW | CS_VREDRAW;  				//改变窗口大小则重画
	wndclass.lpfnWndProc = WndProc;							//窗口函数为WndProc
	wndclass.cbClsExtra = 0;									//窗口类无扩展
	wndclass.cbWndExtra = 0;								//窗口实例无扩展
	wndclass.hInstance = hInstance; 							//注册窗口类实例句柄
	wndclass.hIcon = LoadIcon(NULL, IDI_APPLICATION);			//用箭头光标
	wndclass.hCursor = LoadCursor(NULL, IDC_ARROW);
	wndclass.hbrBackground = (HBRUSH)GetStockObject(WHITE_BRUSH);	//背景为白色
	wndclass.lpszMenuName = NULL;								//窗口默认无菜单
	wndclass.lpszClassName = lpszClassName;
	//注册窗口类型
	if (!RegisterClass(&wndclass))
		return FALSE;

	//创建窗口
	hwnd = CreateWindow(lpszClassName,
		"window窗口创建",
		WS_OVERLAPPEDWINDOW,
		CW_USEDEFAULT, CW_USEDEFAULT,
		CW_USEDEFAULT, CW_USEDEFAULT,
		NULL,
		NULL,
		hInstance,
		NULL);
	//显示并刷新窗口
	ShowWindow(hwnd, nCmdShow);								//显示窗口
	UpdateWindow(hwnd);										//更新窗口的客户区
	//消息循环
	while (GetMessage(&msg, NULL, 0, 0))
	{
		TranslateMessage(&msg);	 							//键盘消息转换
		DispatchMessage(&msg);	 							//派送消息给窗口函数
	}
	return msg.wParam;											//返回退出值
}
//响应窗口消息
LRESULT CALLBACK WndProc(HWND hwnd, UINT message,
	WPARAM wParam,
	LPARAM lParam)
{
	//根据消息值转相应的消息处理
	switch (message)
	{
		//重画窗口客户区消息处理
	case WM_PAINT:
		HDC hdc;		 						//定义设备描述表句柄
		PAINTSTRUCT ps;    					//定义绘图信息结构变量
		hdc = BeginPaint(hwnd, &ps);				//获取要重画的窗口的设备描述表句柄
		//TextOut(hdc,150,150,"这是我自己创建的第一个窗口哦！", 28);	//输出文本

		int i;
		TextOut(hdc, 150, 150, TEXT("**************************"), strlen("**************************"));
		for (i = 1; i < 21; i++)
		{
			TextOut(hdc, 150, 150 + i * 10, TEXT("*                                     *"), strlen("*                                     *"));
		}
		TextOut(hdc, 150, 360, TEXT("**************************"), strlen("**************************"));

		EndPaint(hwnd, &ps);
		break;
		//响应鼠标单击消息
	case WM_LBUTTONDOWN:
	{
		MessageBeep(0);
	}
	break;
	//撤消窗口消息处理 
	case WM_DESTROY:
		PostQuitMessage(0);
		break;
		//其它转缺省窗口函数
	default:
		return DefWindowProc(hwnd, message, wParam, lParam);
	}
	return 0;
}
