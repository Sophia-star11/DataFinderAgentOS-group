"""Crawl4AI 技能执行模块 — 作为 python_func 技能被 SkillExecutor 调用"""

import asyncio
import logging

logger = logging.getLogger("crawl4ai_skill")


def crawl_url(url: str = "", **kwargs) -> dict:
    """
    使用 Crawl4AI 引擎爬取指定 URL 的网页内容（同步包装器）
    返回结构化数据：标题、正文（markdown格式）、成功状态
    """
    if not url:
        return {"success": False, "error": "缺少 URL 参数", "title": "", "content": ""}

    try:
        result = asyncio.run(_async_crawl(url))
        return result
    except Exception as e:
        logger.error(f"Crawl4AI 爬取失败: {e}")
        return {"success": False, "error": str(e), "title": "", "content": ""}


async def _async_crawl(url: str) -> dict:
    """异步执行 Crawl4AI 爬取"""
    from crawl4ai import AsyncWebCrawler

    async with AsyncWebCrawler() as crawler:
        crawl_result = await crawler.arun(url=url)

        if crawl_result and crawl_result.success:
            return {
                "success": True,
                "title": getattr(crawl_result, "title", "") or "",
                "content": (crawl_result.markdown or "")[:8000],
                "url": url
            }
        else:
            error_msg = getattr(crawl_result, "error_message", "未知错误") if crawl_result else "爬取无返回结果"
            return {"success": False, "error": error_msg, "title": "", "content": "", "url": url}
