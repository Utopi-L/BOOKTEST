
// TestThree 3View.cpp: CTestThree3View 类的实现
//

#include "pch.h"
#include "framework.h"
// SHARED_HANDLERS 可以在实现预览、缩略图和搜索筛选器句柄的
// ATL 项目中进行定义，并允许与该项目共享文档代码。
#ifndef SHARED_HANDLERS
#include "TestThree 3.h"
#endif

#include "TestThree 3Doc.h"
#include "TestThree 3View.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// CTestThree3View

IMPLEMENT_DYNCREATE(CTestThree3View, CView)

BEGIN_MESSAGE_MAP(CTestThree3View, CView)
	// 标准打印命令
	ON_COMMAND(ID_FILE_PRINT, &CView::OnFilePrint)
	ON_COMMAND(ID_FILE_PRINT_DIRECT, &CView::OnFilePrint)
	ON_COMMAND(ID_FILE_PRINT_PREVIEW, &CTestThree3View::OnFilePrintPreview)
	ON_WM_CONTEXTMENU()
	ON_WM_RBUTTONUP()
	ON_WM_LBUTTONDOWN()
END_MESSAGE_MAP()

// CTestThree3View 构造/析构

CTestThree3View::CTestThree3View() noexcept
{
	// TODO: 在此处添加构造代码

}

CTestThree3View::~CTestThree3View()
{
}

BOOL CTestThree3View::PreCreateWindow(CREATESTRUCT& cs)
{
	// TODO: 在此处通过修改
	//  CREATESTRUCT cs 来修改窗口类或样式

	return CView::PreCreateWindow(cs);
}

// CTestThree3View 绘图

void CTestThree3View::OnDraw(CDC* /*pDC*/)
{
	CTestThree3Doc* pDoc = GetDocument();
	ASSERT_VALID(pDoc);
	if (!pDoc)
		return;

	// TODO: 在此处为本机数据添加绘制代码
}


// CTestThree3View 打印


void CTestThree3View::OnFilePrintPreview()
{
#ifndef SHARED_HANDLERS
	AFXPrintPreview(this);
#endif
}

BOOL CTestThree3View::OnPreparePrinting(CPrintInfo* pInfo)
{
	// 默认准备
	return DoPreparePrinting(pInfo);
}

void CTestThree3View::OnBeginPrinting(CDC* /*pDC*/, CPrintInfo* /*pInfo*/)
{
	// TODO: 添加额外的打印前进行的初始化过程
}

void CTestThree3View::OnEndPrinting(CDC* /*pDC*/, CPrintInfo* /*pInfo*/)
{
	// TODO: 添加打印后进行的清理过程
}

void CTestThree3View::OnRButtonUp(UINT /* nFlags */, CPoint point)
{
	ClientToScreen(&point);
	OnContextMenu(this, point);
}

void CTestThree3View::OnContextMenu(CWnd* /* pWnd */, CPoint point)
{
#ifndef SHARED_HANDLERS
	theApp.GetContextMenuManager()->ShowPopupMenu(IDR_POPUP_EDIT, point.x, point.y, this, TRUE);
#endif
}


// CTestThree3View 诊断

#ifdef _DEBUG
void CTestThree3View::AssertValid() const
{
	CView::AssertValid();
}

void CTestThree3View::Dump(CDumpContext& dc) const
{
	CView::Dump(dc);
}

CTestThree3Doc* CTestThree3View::GetDocument() const // 非调试版本是内联的
{
	ASSERT(m_pDocument->IsKindOf(RUNTIME_CLASS(CTestThree3Doc)));
	return (CTestThree3Doc*)m_pDocument;
}
#endif //_DEBUG


// CTestThree3View 消息处理程序


void CTestThree3View::OnLButtonDown(UINT nFlags, CPoint point)
{
	POINT mousePos;
	int mx, my;
	GetCursorPos(&mousePos);
	ScreenToClient(&mousePos);
	mx = mousePos.x;
	my = mousePos.y;
	CClientDC dc(this);
	dc.MoveTo(10, 10);

	dc.LineTo(mx, 10);
	dc.LineTo(mx, my);
	dc.LineTo(10, my);
	dc.LineTo(10, 10);
	// TODO: 在此添加消息处理程序代码和/或调用默认值

	CView::OnLButtonDown(nFlags, point);

}