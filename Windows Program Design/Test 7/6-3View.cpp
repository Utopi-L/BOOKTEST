
// 实验6-3View.cpp: C实验63View 类的实现
//

#include "pch.h"
#include "framework.h"
// SHARED_HANDLERS 可以在实现预览、缩略图和搜索筛选器句柄的
// ATL 项目中进行定义，并允许与该项目共享文档代码。
#ifndef SHARED_HANDLERS
#include "实验6-3.h"
#endif

#include "实验6-3Doc.h"
#include "实验6-3View.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// C实验63View

IMPLEMENT_DYNCREATE(C实验63View, CView)

BEGIN_MESSAGE_MAP(C实验63View, CView)
	// 标准打印命令
	ON_MESSAGE(WM_MYMSG,OnMyMsg)
	ON_COMMAND(ID_FILE_PRINT, &CView::OnFilePrint)
	ON_COMMAND(ID_FILE_PRINT_DIRECT, &CView::OnFilePrint)
	ON_COMMAND(ID_FILE_PRINT_PREVIEW, &C实验63View::OnFilePrintPreview)
	ON_WM_CONTEXTMENU()
	ON_WM_RBUTTONUP()
END_MESSAGE_MAP()

// C实验63View 构造/析构

C实验63View::C实验63View() noexcept
{
	// TODO: 在此处添加构造代码

}

C实验63View::~C实验63View()
{
}

BOOL C实验63View::PreCreateWindow(CREATESTRUCT& cs)
{
	// TODO: 在此处通过修改
	//  CREATESTRUCT cs 来修改窗口类或样式

	return CView::PreCreateWindow(cs);
}

// C实验63View 绘图

void C实验63View::OnDraw(CDC* /*pDC*/)
{
	C实验63Doc* pDoc = GetDocument();
	ASSERT_VALID(pDoc);
	if (!pDoc)
		return;

	// TODO: 在此处为本机数据添加绘制代码
}


// C实验63View 打印


void C实验63View::OnFilePrintPreview()
{
#ifndef SHARED_HANDLERS
	AFXPrintPreview(this);
#endif
}

BOOL C实验63View::OnPreparePrinting(CPrintInfo* pInfo)
{
	// 默认准备
	return DoPreparePrinting(pInfo);
}

void C实验63View::OnBeginPrinting(CDC* /*pDC*/, CPrintInfo* /*pInfo*/)
{
	// TODO: 添加额外的打印前进行的初始化过程
}

void C实验63View::OnEndPrinting(CDC* /*pDC*/, CPrintInfo* /*pInfo*/)
{
	// TODO: 添加打印后进行的清理过程
}

void C实验63View::OnRButtonUp(UINT /* nFlags */, CPoint point)
{
	ClientToScreen(&point);
	OnContextMenu(this, point);
}

void C实验63View::OnContextMenu(CWnd* /* pWnd */, CPoint point)
{
#ifndef SHARED_HANDLERS
	theApp.GetContextMenuManager()->ShowPopupMenu(IDR_POPUP_EDIT, point.x, point.y, this, TRUE);
#endif
}


// C实验63View 诊断

#ifdef _DEBUG
void C实验63View::AssertValid() const
{
	CView::AssertValid();
}

void C实验63View::Dump(CDumpContext& dc) const
{
	CView::Dump(dc);
}

C实验63Doc* C实验63View::GetDocument() const // 非调试版本是内联的
{
	ASSERT(m_pDocument->IsKindOf(RUNTIME_CLASS(C实验63Doc)));
	return (C实验63Doc*)m_pDocument;
}
#endif //_DEBUG


// C实验63View 消息处理程序
int C实验63View::OnMyMsg(WPARAM wParam, LPARAM lParam)
{
	char* name = new char[50];
	name = (char*)wParam;
	m_name.Format(_T("%s"), name);
	char* add = new char[50];
	add = (char*)lParam;
	m_add.Format(_T("%s"), add);
	UpdateData(FALSE);
	Invalidate();
	return 0;
}