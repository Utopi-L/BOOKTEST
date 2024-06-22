
// 实验5-1View.cpp: C实验51View 类的实现
//

#include "pch.h"
#include"cstring"
#include "framework.h"
// SHARED_HANDLERS 可以在实现预览、缩略图和搜索筛选器句柄的
// ATL 项目中进行定义，并允许与该项目共享文档代码。
#ifndef SHARED_HANDLERS
#include "实验5-1.h"
#endif

#include "实验5-1Doc.h"
#include "实验5-1View.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// C实验51View

IMPLEMENT_DYNCREATE(C实验51View, CView)

BEGIN_MESSAGE_MAP(C实验51View, CView)
	// 标准打印命令
	ON_COMMAND(ID_FILE_PRINT, &CView::OnFilePrint)
	ON_COMMAND(ID_FILE_PRINT_DIRECT, &CView::OnFilePrint)
	ON_COMMAND(ID_FILE_PRINT_PREVIEW, &CView::OnFilePrintPreview)
END_MESSAGE_MAP()

// C实验51View 构造/析构

C实验51View::C实验51View() noexcept
{
	// TODO: 在此处添加构造代码

}

C实验51View::~C实验51View()
{
}

BOOL C实验51View::PreCreateWindow(CREATESTRUCT& cs)
{
	// TODO: 在此处通过修改
	//  CREATESTRUCT cs 来修改窗口类或样式

	return CView::PreCreateWindow(cs);
}

// C实验51View 绘图

void C实验51View::OnDraw(CDC* pDC)
{
	C实验51Doc* pDoc = GetDocument();
	ASSERT_VALID(pDoc);
	// TODO: add draw code for native data here
		//当前文本颜色
	COLORREF crOld;
	//设置文本颜色
	crOld = pDC->SetTextColor(RGB(255, 0, 0));
	//输出文本
	pDC->TextOut(100, 80, "这就是想要输出的文本字符串");
	//恢复默认文本颜色
	

}


// C实验51View 打印

BOOL C实验51View::OnPreparePrinting(CPrintInfo* pInfo)
{
	// 默认准备
	return DoPreparePrinting(pInfo);
}

void C实验51View::OnBeginPrinting(CDC* /*pDC*/, CPrintInfo* /*pInfo*/)
{
	// TODO: 添加额外的打印前进行的初始化过程
}

void C实验51View::OnEndPrinting(CDC* /*pDC*/, CPrintInfo* /*pInfo*/)
{
	// TODO: 添加打印后进行的清理过程
}


// C实验51View 诊断

#ifdef _DEBUG
void C实验51View::AssertValid() const
{
	CView::AssertValid();
}

void C实验51View::Dump(CDumpContext& dc) const
{
	CView::Dump(dc);
}

C实验51Doc* C实验51View::GetDocument() const // 非调试版本是内联的
{
	ASSERT(m_pDocument->IsKindOf(RUNTIME_CLASS(C实验51Doc)));
	return (C实验51Doc*)m_pDocument;
}
#endif //_DEBUG


// C实验51View 消息处理程序
