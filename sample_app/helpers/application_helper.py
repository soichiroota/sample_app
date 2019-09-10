def full_title(page_title=''):
    """ページごとの完全なタイトルを返します。"""
    base_title = 'Django Tutorial Sample App'
    if page_title:
        return page_title + ' | ' + base_title
    else:
        return base_title