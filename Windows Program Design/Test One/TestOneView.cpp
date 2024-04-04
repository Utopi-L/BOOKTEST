
// TestOneView.cpp: CTestOneView 类的实现
//

#include "pch.h"
#include "framework.h"
// SHARED_HANDLERS 可以在实现预览、缩略图和搜索筛选器句柄的
// ATL 项目中进行定义，并允许与该项目共享文档代码。
#ifndef SHARED_HANDLERS
#include "TestOne.h"
#endif

#include "TestOneDoc.h"
#include "TestOneView.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// CTestOneView

IMPLEMENT_DYNCREATE(CTestOneView, CView)

BEGIN_MESSAGE_MAP(CTestOneView, CView)
	// 标准打印命令
	ON_COMMAND(ID_FILE_PRINT, &CView::OnFilePrint)
	ON_COMMAND(ID_FILE_PRINT_DIRECT, &CView::OnFilePrint)
	ON_COMMAND(ID_FILE_PRINT_PREVIEW, &CTestOneView::OnFilePrintPreview)
	ON_WM_CONTEXTMENU()
	ON_WM_RBUTTONUP()
END_MESSAGE_MAP()

// CTestOneView 构造/析构

CTestOneView::CTestOneView() noexcept
{
	// TODO: 在此处添加构造代码

}

CTestOneView::~CTestOneView()
{
}

BOOL CTestOneView::PreCreateWindow(CREATESTRUCT& cs)
{
	// TODO: 在此处通过修改
	//  CREATESTRUCT cs 来修改窗口类或样式

	return CView::PreCreateWindow(cs);
}

// CTestOneView 绘图

void CTestOneView::OnDraw(CDC* pDC)
{
	CTestOneDoc* pDoc = GetDocument();
	ASSERT_VALID(pDoc);
	if (!pDoc)
		return;
	pDC->RoundRect(55, 20, 160, 100, 20, 15);
	// TODO: 在此处为本机数据添加绘制代码
}


// CTestOneView 打印


void CTestOneView::OnFilePrintPreview()
{
#ifndef SHARED_HANDLERS
	AFXPrintPreview(this);
#endif
}

BOOL CTestOneView::OnPreparePrinting(CPrintInfo* pInfo)
{
	// 默认准备
	return DoPreparePrinting(pInfo);
}

void CTestOneView::OnBeginPrinting(CDC* /*pDC*/, CPrintInfo* /*pInfo*/)
{
	// TODO: 添加额外的打印前进行的初始化过程
}

void CTestOneView::OnEndPrinting(CDC* /*pDC*/, CPrintInfo* /*pInfo*/)
{
	// TODO: 添加打印后进行的清理过程
}

void CTestOneView::OnRButtonUp(UINT /* nFlags */, CPoint point)
{
	ClientToScreen(&point);
	OnContextMenu(this, point);
}

void CTestOneView::OnContextMenu(CWnd* /* pWnd */, CPoint point)
{
#ifndef SHARED_HANDLERS
	theApp.GetContextMenuManager()->ShowPopupMenu(IDR_POPUP_EDIT, point.x, point.y, this, TRUE);
#endif
}


// CTestOneView 诊断

#ifdef _DEBUG
void CTestOneView::AssertValid() const
{
	CView::AssertValid();
}

void CTestOneView::Dump(CDumpContext& dc) const
{
	CView::Dump(dc);
}

CTestOneDoc* CTestOneView::GetDocument() const // 非调试版本是内联的
{
	ASSERT(m_pDocument->IsKindOf(RUNTIME_CLASS(CTestOneDoc)));
	return (CTestOneDoc*)m_pDocument;
}
#endif //_DEBUG


// CTestOneView 消息处理程序
