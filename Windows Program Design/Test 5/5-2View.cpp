
// 实验5-2View.cpp: C实验52View 类的实现
//

#include "pch.h"
#include "framework.h"
// SHARED_HANDLERS 可以在实现预览、缩略图和搜索筛选器句柄的
// ATL 项目中进行定义，并允许与该项目共享文档代码。
#ifndef SHARED_HANDLERS
#include "实验5-2.h"
#endif

#include "实验5-2Doc.h"
#include "实验5-2View.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// C实验52View

IMPLEMENT_DYNCREATE(C实验52View, CView)

BEGIN_MESSAGE_MAP(C实验52View, CView)
	// 标准打印命令
	ON_COMMAND(ID_FILE_PRINT, &CView::OnFilePrint)
	ON_COMMAND(ID_FILE_PRINT_DIRECT, &CView::OnFilePrint)
	ON_COMMAND(ID_FILE_PRINT_PREVIEW, &C实验52View::OnFilePrintPreview)
	ON_WM_CONTEXTMENU()
	ON_WM_RBUTTONUP()
END_MESSAGE_MAP()

// C实验52View 构造/析构

C实验52View::C实验52View() noexcept
{
	// TODO: 在此处添加构造代码

}

C实验52View::~C实验52View()
{
}

BOOL C实验52View::PreCreateWindow(CREATESTRUCT& cs)
{
	// TODO: 在此处通过修改
	//  CREATESTRUCT cs 来修改窗口类或样式

	return CView::PreCreateWindow(cs);
}

// C实验52View 绘图

void C实验52View::OnDraw(CDC* pDC)
{
	C实验52Doc* pDoc = GetDocument();
	ASSERT_VALID(pDoc);
	if (!pDoc)
		return;

	CString str;
	str.Format("这就是想要输出的文本字符串");
	pDC->SelectStockObject(SYSTEM_FONT);
	pDC->TextOut(100, 100, str);
	//获取字符串的高度和宽度并输出
	CSize size = pDC->GetTextExtent(str);
	str.Format("输出字符的宽度和高度：%d×%d", size.cx, size.cy);
	pDC->TextOut(100, 150, str);// TODO: 在此处为本机数据添加绘制代码
}


// C实验52View 打印


void C实验52View::OnFilePrintPreview()
{
#ifndef SHARED_HANDLERS
	AFXPrintPreview(this);
#endif
}

BOOL C实验52View::OnPreparePrinting(CPrintInfo* pInfo)
{
	// 默认准备
	return DoPreparePrinting(pInfo);
}

void C实验52View::OnBeginPrinting(CDC* /*pDC*/, CPrintInfo* /*pInfo*/)
{
	// TODO: 添加额外的打印前进行的初始化过程
}

void C实验52View::OnEndPrinting(CDC* /*pDC*/, CPrintInfo* /*pInfo*/)
{
	// TODO: 添加打印后进行的清理过程
}

void C实验52View::OnRButtonUp(UINT /* nFlags */, CPoint point)
{
	ClientToScreen(&point);
	OnContextMenu(this, point);
}

void C实验52View::OnContextMenu(CWnd* /* pWnd */, CPoint point)
{
#ifndef SHARED_HANDLERS
	theApp.GetContextMenuManager()->ShowPopupMenu(IDR_POPUP_EDIT, point.x, point.y, this, TRUE);
#endif
}


// C实验52View 诊断

#ifdef _DEBUG
void C实验52View::AssertValid() const
{
	CView::AssertValid();
}

void C实验52View::Dump(CDumpContext& dc) const
{
	CView::Dump(dc);
}

C实验52Doc* C实验52View::GetDocument() const // 非调试版本是内联的
{
	ASSERT(m_pDocument->IsKindOf(RUNTIME_CLASS(C实验52Doc)));
	return (C实验52Doc*)m_pDocument;
}
#endif //_DEBUG


// C实验52View 消息处理程序
