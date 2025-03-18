
// 实验7-2View.cpp: C实验72View 类的实现
//

#include "pch.h"
#include "framework.h"
// SHARED_HANDLERS 可以在实现预览、缩略图和搜索筛选器句柄的
// ATL 项目中进行定义，并允许与该项目共享文档代码。
#ifndef SHARED_HANDLERS
#include "实验7-2.h"
#endif

#include "实验7-2Doc.h"
#include "实验7-2View.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// C实验72View

IMPLEMENT_DYNCREATE(C实验72View, CView)

BEGIN_MESSAGE_MAP(C实验72View, CView)
	// 标准打印命令
	ON_COMMAND(ID_FILE_PRINT, &CView::OnFilePrint)
	ON_COMMAND(ID_FILE_PRINT_DIRECT, &CView::OnFilePrint)
	ON_COMMAND(ID_FILE_PRINT_PREVIEW, &C实验72View::OnFilePrintPreview)
	ON_WM_CONTEXTMENU()
	ON_WM_RBUTTONUP()
	ON_WM_KEYDOWN()
END_MESSAGE_MAP()

// C实验72View 构造/析构

C实验72View::C实验72View() noexcept
{
	// TODO: 在此处添加构造代码

}

C实验72View::~C实验72View()
{
}

BOOL C实验72View::PreCreateWindow(CREATESTRUCT& cs)
{
	// TODO: 在此处通过修改
	//  CREATESTRUCT cs 来修改窗口类或样式

	return CView::PreCreateWindow(cs);
}

// C实验72View 绘图

void C实验72View::OnDraw(CDC*pDC)
{
	C实验72Doc* pDoc = GetDocument();
	ASSERT_VALID(pDoc);
	if (!pDoc)
		return;

	pDC->Ellipse(pDoc->m_rect);// TODO: 在此处为本机数据添加绘制代码
}


// C实验72View 打印


void C实验72View::OnFilePrintPreview()
{
#ifndef SHARED_HANDLERS
	AFXPrintPreview(this);
#endif
}

BOOL C实验72View::OnPreparePrinting(CPrintInfo* pInfo)
{
	// 默认准备
	return DoPreparePrinting(pInfo);
}

void C实验72View::OnBeginPrinting(CDC* /*pDC*/, CPrintInfo* /*pInfo*/)
{
	// TODO: 添加额外的打印前进行的初始化过程
}

void C实验72View::OnEndPrinting(CDC* /*pDC*/, CPrintInfo* /*pInfo*/)
{
	// TODO: 添加打印后进行的清理过程
}

void C实验72View::OnRButtonUp(UINT /* nFlags */, CPoint point)
{
	ClientToScreen(&point);
	OnContextMenu(this, point);
}

void C实验72View::OnContextMenu(CWnd* /* pWnd */, CPoint point)
{
#ifndef SHARED_HANDLERS
	theApp.GetContextMenuManager()->ShowPopupMenu(IDR_POPUP_EDIT, point.x, point.y, this, TRUE);
#endif
}


// C实验72View 诊断

#ifdef _DEBUG
void C实验72View::AssertValid() const
{
	CView::AssertValid();
}

void C实验72View::Dump(CDumpContext& dc) const
{
	CView::Dump(dc);
}

C实验72Doc* C实验72View::GetDocument() const // 非调试版本是内联的
{
	ASSERT(m_pDocument->IsKindOf(RUNTIME_CLASS(C实验72Doc)));
	return (C实验72Doc*)m_pDocument;
}
#endif //_DEBUG


// C实验72View 消息处理程序


void C实验72View::OnKeyDown(UINT nChar, UINT nRepCnt, UINT nFlags)
{
	C实验72Doc* pDoc = GetDocument();
	CRect rt;
	GetClientRect(&rt);				//获取当前的绘图区域
	switch (nChar)
	{
	case VK_SHIFT:				//如果按下的是向左的箭头"←"
		
		AfxMessageBox("您按下了shift键");
		break;
	case VK_RIGHT:				//如果按下的是向右的箭头"→"
		AfxMessageBox("您按下了→键");
		break;
	case VK_UP:					//如果按下的是向上的箭头"↑"
		
		AfxMessageBox("您按下了↑键");
		break;
	case VK_DOWN:				//如果按下的是向下的箭头"↓"
		AfxMessageBox("您按下了↓键");
		break;
	case VK_LEFT:
		AfxMessageBox("您按下了←键");
	}
	InvalidateRect(NULL, TRUE);		//刷新窗口	

	CView::OnKeyDown(nChar, nRepCnt, nFlags);// TODO: 在此添加消息处理程序代码和/或调用默认值

	
}
