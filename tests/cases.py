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

对于 newline，主要考虑 body elements，包括：

    1. Paragraphs
    #. Lists

       a) Bullet lists
       #) Enumerated lists
       #) Definition lists
       #) Field lists
       #) Option lists

    #. Literal blocks
    #. Block quotes
    #. Tables

       a) Grid tables
       #) Simple tables

    #. Inline Markup

       a) Emphasis
       #) Strong Emphasis
       #) Interpreted text
       #) Inline literals
       #) Substitution reference
       #) Inline internal targets
       #) Footnote reference
       #) Citation reference
       #) Hyperlink reference
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

# original: expected
NEWLINE_CASES = {
# paragraphs
'''<p>中文换行
不应该导致空格。</p>''':
'''<p>中文换行不应该导致空格。</p>''',
'''<p>English newline
resulting in backspace.</p>''':
'''<p>English newline resulting in backspace.</p>''',
# bullet lists
'''<ul>
<li><p class="first">列表：中文换行
不应该导致空格</p>
</li>
<li><p class="first">列表</p>
<p>中文换行
不应该导致空格</p>
</li>
</ul>''':
'''<ul>
<li><p class="first">列表：中文换行不应该导致空格</p>
</li>
<li><p class="first">列表</p>
<p>中文换行不应该导致空格</p>
</li>
</ul>''',
# enumerated lists
'''<ol class="arabic">
<li><p class="first">列表：中文换行
不应该导致空格</p>
</li>
<li><p class="first">列表</p>
<p>中文换行
不应该导致空格</p>
</li>
</ol>''':
'''<ol class="arabic">
<li><p class="first">列表：中文换行不应该导致空格</p>
</li>
<li><p class="first">列表</p>
<p>中文换行不应该导致空格</p>
</li>
</ol>''',
# definition lists
'''<dl class="docutils">
<dt>定义</dt>
<dd>中文换行
不应该导致换行</dd>
</dl>''':
'''<dl class="docutils">
<dt>定义</dt>
<dd>中文换行不应该导致换行</dd>
</dl>''',
# field lists
'''<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">领域:</th><td class="field-body">中文换行
不应该导致空格</td>
</tr>
</tbody>
</table>''':
'''<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">领域:</th><td class="field-body">中文换行不应该导致空格</td>
</tr>
</tbody>
</table>''',
# option lists
'''<table class="docutils option-list" frame="void" rules="none">
<col class="option" />
<col class="description" />
<tbody valign="top">
<tr><td class="option-group">
<kbd><span class="option">-a</span></kbd></td>
<td>中文换行
不应该导致空格</td></tr>
</tbody>
</table>''':
'''<table class="docutils option-list" frame="void" rules="none">
<col class="option" />
<col class="description" />
<tbody valign="top">
<tr><td class="option-group">
<kbd><span class="option">-a</span></kbd></td>
<td>中文换行不应该导致空格</td></tr>
</tbody>
</table>''',
# literal blocks
'''<p>接下来的一段内容是 literal blocks，应该
保持原格式:</p>
<div class="highlight-python"><div class="highlight"><pre>这段内容的格式
    不应该有任何变化
</pre></div>
</div>
</div>''':
'''<p>接下来的一段内容是 literal blocks，应该
保持原格式:</p>
<div class="highlight-python"><div class="highlight"><pre>这段内容的格式
    不应该有任何变化
</pre></div>
</div>
</div>''',
# block quotes
'''<p>接下来的一段是 block quotes</p>
<blockquote>
<div><p>我要这天，
再遮不住我眼！</p>
<p class="attribution">&mdash;逗比式</p>
</div></blockquote>''':
'''<p>接下来的一段是 block quotes</p>
<blockquote>
<div><p>我要这天，再遮不住我眼！</p>
<p class="attribution">&mdash;逗比式</p>
</div></blockquote>''',
# grid tables
'''<table border="1" class="docutils">
<colgroup>
<col width="58%" />
<col width="42%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">表头，中文换行
不应该导致空格</th>
<th class="head">表头</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td>表身</td>
<td>中文换行
不应该导致空格</td>
</tr>
</tbody>
</table>''';
'''<table border="1" class="docutils">
<colgroup>
<col width="58%" />
<col width="42%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">表头，中文换行不应该导致空格</th>
<th class="head">表头</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td>表身</td>
<td>中文换行不应该导致空格</td>
</tr>
</tbody>
</table>''',
# simple table
'''<table border="1" class="docutils">
<colgroup>
<col width="58%" />
<col width="42%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">表头</th>
<th class="head">表头</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td>表身</td>
<td>中文换行
不应该导致空格</td>
</tr>
</tbody>
</table>''';
'''<table border="1" class="docutils">
<colgroup>
<col width="58%" />
<col width="42%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">表头</th>
<th class="head">表头</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td>表身</td>
<td>中文换行不应该导致空格</td>
</tr>
</tbody>
</table>''',
# emphasis
'''<p>中文前
<em>中文换行
不应该导致空格</em>
中文后</p>''':
'''<p>中文前<em>中文换行不应该导致空格</em>中文后</p>''',
# strong emphasis
'''<p>中文前
<strong>中文换行
不应该导致空格</strong>
中文后</p>''';
'''<p>中文前<strong>中文换行不应该导致空格</strong>中文后</p>''',
# interpreted text
'''<p>中文前
<cite>中文换行
不应该导致空格</cite>
中文后</p>''';
'''<p>中文前<cite>中文换行不应该导致空格</cite>中文后</p>''',
# inline literals
'''<p>中文前
<span class="docutils literal"><span class="pre">中文换行</span>
<span class="pre">不应该导致空格</span></span>
中文后</p>''':
'''<p>中文前<span class="docutils literal"><span class="pre">中文换行</span><span class="pre">不应该导致空格</span></span>中文后</p>''',
# substituation reference
'''<p>中文前
中文换行
不应该导致空格
中文后</p>''':
'''<p>中文前中文换行不应该导致空格中文后</p>''',
# footnotes
'''<table class="docutils footnote" frame="void" id="id9" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label">[1]</td><td>中文换行
不应该导致空格</td></tr>
</tbody>
</table>''':
'''<table class="docutils footnote" frame="void" id="id9" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label">[1]</td><td>中文换行不应该导致空格</td></tr>
</tbody>
</table>''',
# citation
'''<table class="docutils citation" frame="void" id="cit2002" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label">[CIT2002]</td><td>中文换行
不应导致空格</td></tr>
</tbody>
</table>''':
'''<table class="docutils citation" frame="void" id="cit2002" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label">[CIT2002]</td><td>中文换行不应导致空格</td></tr>
</tbody>
</table>''',
# hyperlink reference
'''<p>中文前
<a class="reference external" href="http://www.zhihu.com">中文换行
不应该导致空格5</a>
中文后</p>''':
'''<p>中文前<a class="reference external" href="http://www.zhihu.com">中文换行不应该导致空格5</a>中文后</p>''',
}
