
// 实验6-3View.h: C实验63View 类的接口
//

#pragma once


class C实验63View : public CView
{
protected: // 仅从序列化创建
	C实验63View() noexcept;
	DECLARE_DYNCREATE(C实验63View)
public:
	CString m_name;
	CString m_add;
public:
	afx_msg int OnMyMsg(WPARAM wParam, LPARAM lParam);
	DECLARE_MESSAGE_MAP()
// 特性
public:
	C实验63Doc* GetDocument() const;

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
	virtual ~C实验63View();
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
};

#ifndef _DEBUG  // 实验6-3View.cpp 中的调试版本
inline C实验63Doc* C实验63View::GetDocument() const
   { return reinterpret_cast<C实验63Doc*>(m_pDocument); }
#endif

