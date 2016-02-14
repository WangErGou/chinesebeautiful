# -*- coding:utf-8 -*-

'''
rST 支持的 Inline Markup 一共有9种，分别是：

    1. *emphasis*
    #. **strong emphasis**
    #. `interpreted text`
    #. ``inline literal``
    #. |substituation reference|
    #. _`inline internal target`
    #. footnote reference [1]_
    #. reference_
    #. `phrase reference`_

其中，footnote reference 不用考虑多余空格的问题。
'''

# original: expecetd
INLINE_MARKUP_CASES = {
    # inline marker 的内容是中文还是英文？
    # inline marker 左|右的元素内容是中文，英文还是标点符号？
    '<p>中文前 <em>emphasis</em> 中文后</p>': '<p>中文前 <em>emphasis</em> 中文后</p>',
    '<p>中文前 <strong>strong emphasis</strong> 中文后</p>': '<p>中文前 <strong>strong emphasis</strong> 中文后</p>',
    '<p>中文前 <cite>interpreted text</cite> 中文后</p>': '<p>中文前 <cite>interpreted text</cite> 中文后</p>',
    '<p>中文前 <span class="docutils literal"><span class="pre">inline</span> <span class="pre">literal</span></span> 中文后</p>': '<p>中文前 <span class="docutils literal"><span
    class="pre">inline</span> <span class="pre">literal</span></span> 中文后</p>',
    '<p>中文前 substituation reference 中文后</p>': '<p>中文前 substituation reference 中文后</p>',
    '<p>中文前 <span class="target" id="inline-internal-target">inline internal target</span> 中文后</p>': '<p>中文前 <span class="target" id="inline-internal-target">inline internal target</span> 中文后</p>',
    '<p>中文前 <a class="reference external" href="http://www.zhihu.com">reference</a> 中文后</p>': '<p>中文前 <a class="reference external" href="http://www.zhihu.com">reference</a> 中文后</p>',
    '<p>中文前 <a class="reference external" href="http://www.zhihu.com">phrase reference</a> 中文后</p>': '<p>中文前 <a class="reference external" href="http://www.zhihu.com">phrase reference</a> 中文后</p>',

    '<p>中文前 <em>斜体</em> 中文后</p>': '<p>中文前<em>斜体</em>中文后</p>',
    '<p>中文前 <strong>加粗</strong> 中文后</p>': '<p>中文前<strong>加粗</strong>中文后</p>',
    '<p>中文前 <cite>解释文</cite> 中文后</p>': '<p>中文前<cite>解释文</cite>中文后</p>',
    '<p>中文前 <span class="docutils literal"><span class="pre">段内自由文</span></span> 中文后</p>': '<p>中文前<span class="docutils literal"><span class="pre">段内自由文</span></span>中文后</p>',
    '<p>中文前 替换引用内容 中文后</p>': '<p>中文前替换引用内容中文后</p>',
    '<p>中文前 <span class="target" id="id1">段内内部引用</span> 中文后</p>': '<p>中文前<span class="target" id="id1">段内内部引用</span>中文后</p>',
    '<p>中文前 <a href="#id4"><span class="problematic" id="id5">引用__</span></a> 中文后</p>': '<p>中文前<a href="#id4"><span class="problematic" id="id5">引用__</span></a>中文后</p>',
    '<p>中文前 <a class="reference external" href="http://www.zhihu.com">带解释的引用</a> 中文后</p>': '<p>中文前<a class="reference external" href="http://www.zhihu.com">带解释的引用</a>中文后</p>',

    '<p>English <em>斜体</em> 中文后</p>': '<p>English <em>斜体</em>中文后</p>',
    '<p>， <strong>加粗</strong> 中文后</p>': '<p>，<strong>加粗</strong>中文后</p>',
    '<p>。 <cite>解释文</cite> 中文后</p>': '<p>。<cite>解释文</cite>中文后</p>',
    '<p>！ <span class="docutils literal"><span class="pre">段内自由文</span></span> 中文后</p>': '<p>！<span class="docutils literal"><span class="pre">段内自由文</span></span>中文后</p>',
    '<p>1 替换引用内容 中文后</p>': '<p>1替换引用内容中文后</p>',
    '<p>？ <span class="target" id="id3">段内内部引用2</span> 中文后</p>': '<p>？<span class="target" id="id3">段内内部引用2</span>中文后</p>',
    '<p>“ <a href="#id8"><span class="problematic" id="id10">引用__</span></a> 中文后</p>': '<p>“<a href="#id8"><span class="problematic" id="id10">引用__</span></a>中文后</p>',
    '<p>” <a class="reference external" href="http://www.zhihu.com">带解释的引用</a> 中文后</p>': '<p>”<a class="reference external" href="http://www.zhihu.com">带解释的引用</a>中文后</p>',

    '<p>中文前 <em>斜体</em> English</p>': '<p>中文前<em>斜体</em> English</p>',
    '<p>中文前 <strong>加粗</strong> ，</p>': '<p>中文前<strong>加粗</strong>，</p>',
    '<p>中文前 <cite>解释文</cite> 。</p>': '<p>中文前<cite>解释文</cite>。</p>',
    '<p>中文前 <span class="docutils literal"><span class="pre">段内自由文</span></span> ！</p>': '<p>中文前<span class="docutils literal"><span class="pre">段内自由文</span></span>！</p>',
    '<p>中文前 替换引用内容 1</p>': '<p>中文前替换引用内容1</p>',
    '<p>中文前 <span class="target" id="id5">段内内部引用3</span> ？</p>': '<p>中文前<span class="target" id="id5">段内内部引用3</span>？</p>',
    '<p>中文前 <a href="#id8"><span class="problematic" id="id11">引用__</span></a> “</p>': '<p>中文前<a href="#id8"><span class="problematic" id="id11">引用__</span></a>“</p>',
    '<p>中文前 <a class="reference external" href="http://www.zhihu.com">带解释的引用</a> ”</p>': '<p>中文前<a class="reference external" href="http://www.zhihu.com">带解释的引用</a>”</p>',
}
