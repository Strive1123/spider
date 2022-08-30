import requests

headers={
    'Cookie':'_octo=GH1.1.586359234.1658902849; tz=Asia%2FShanghai; _device_id=7c60214ca38d6a3b57a1c6cbfadc54d3; user_session=BvW4ToA0kpDZKzUka0Xc7jDCYEc17pnJMcLVzwoVdQ1PDW8D; __Host-user_session_same_site=BvW4ToA0kpDZKzUka0Xc7jDCYEc17pnJMcLVzwoVdQ1PDW8D; tz=Asia%2FShanghai; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; logged_in=yes; dotcom_user=Strive1123; has_recent_activity=1; _gh_sess=Tjlugqr7fvDz%2FPWZf9a0xA7ib3yMQum5O6Dt4V5eKf%2BP%2BbDcBdjqd5HDakzgFL%2F3ImcwCE%2BMIsoOV04NL2ubb1OJ0i%2FVjVh3apXQctj%2BpUzsFrFRMn48wfFFh5BKYf0WoefIWn6cVr0QSEc4ZS1BuOO11Fj7zN4RQImnITeiixBuWajqxxVVCdzRmdTL9xaitqfx4Y1GW74weARWgN1nFyhsQ5EI%2BjUl--jUjpM3G79naVCX%2Bb--ZGLvmLPblU%2FaMbiJJaLFVw%3D%3D; preferred_color_mode=dark',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

r = requests.get('https://github.com/',headers=headers)
print(r.text)