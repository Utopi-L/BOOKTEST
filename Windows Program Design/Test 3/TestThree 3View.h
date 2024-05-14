﻿
// TestThree 3View.h: CTestThree3View 类的接口
//

#pragma once


class CTestThree3View : public CView
{
protected: // 仅从序列化创建
	CTestThree3View() noexcept;
	DECLARE_DYNCREATE(CTestThree3View)

// 特性
public:
	CTestThree3Doc* GetDocument() const;

// 操作
public:

// 重写
public:
	virtual void OnDraw(CDC* pDC);  // 重写以绘制该视图
	virtual BOOL PreCreateWindow(CREATESTRUCT& cs);
protected:
	virtual BOOL OnPreparePrinting(CPrintInfo* pInfo);
	virtual void OnBeginPrinting(CDC* pDC, CPrintInfo* pInfo);
	virtual void OnEndPrinting(CDC* pDC, CPrintInfo* pInfo);

// 实现
public:
	virtual ~CTestThree3View();
#ifdef _DEBUG
	virtual void AssertValid() const;
	virtual void Dump(CDumpContext& dc) const;
#endif

protected:

// 生成的消息映射函数
protected:
	afx_msg void OnFilePrintPreview();
	afx_msg void OnRButtonUp(UINT nFlags, CPoint point);
	afx_msg void OnContextMenu(CWnd* pWnd, CPoint point);
	DECLARE_MESSAGE_MAP()
public:
	afx_msg void OnLButtonDown(UINT nFlags, CPoint point);
};

#ifndef _DEBUG  // TestThree 3View.cpp 中的调试版本
inline CTestThree3Doc* CTestThree3View::GetDocument() const
   { return reinterpret_cast<CTestThree3Doc*>(m_pDocument); }
#endif

