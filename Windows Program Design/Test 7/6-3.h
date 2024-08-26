
// 实验6-3.h: 实验6-3 应用程序的主头文件
//
#pragma once
#define WM_MYMSG WM_USER+100
#ifndef __AFXWIN_H__
	#error "在包含此文件之前包含 'pch.h' 以生成 PCH"
#endif

#include "resource.h"       // 主符号


// C实验63App:
// 有关此类的实现，请参阅 实验6-3.cpp
//

class C实验63App : public CWinAppEx
{
public:
	C实验63App() noexcept;


// 重写
public:
	virtual BOOL InitInstance();
	virtual int ExitInstance();

// 实现
	UINT  m_nAppLook;
	BOOL  m_bHiColorIcons;

	virtual void PreLoadState();
	virtual void LoadCustomState();
	virtual void SaveCustomState();

	afx_msg void OnAppAbout();
	DECLARE_MESSAGE_MAP()
};

extern C实验63App theApp;
