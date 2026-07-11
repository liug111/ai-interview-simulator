#!/usr/bin/env python3
"""AI面试模拟官 - 简历解析（<150行）"""
import json, os, re

SECTIONS = {
    "contact": ["联系方式", "电话", "手机", "邮箱", "email", "phone"],
    "education": ["教育背景", "教育", "学历", "学校", "大学", "education"],
    "experience": ["工作经历", "工作经验", "工作", "经历", "experience"],
    "projects": ["项目", "projects"],
    "skills": ["专业技能", "技能", "技术栈", "专长", "skills"],
    "summary": ["个人简介", "简介", "概述", "关于我", "summary"]
}


def parse(text):
    lines = text.split("\n")
    bounds = {}
    cur, start = None, 0
    for i, line in enumerate(lines):
        s = line.strip()
        if not s:
            continue
        matched = None
        for sec, kws in SECTIONS.items():
            if any(kw in s for kw in kws) and len(s) < 30:
                matched = sec
                break
        if matched:
            if cur:
                bounds[cur] = (start, i)
            cur, start = matched, i
    if cur:
        bounds[cur] = (start, len(lines))

    def sec(name):
        if name in bounds:
            s, e = bounds[name]
            return "\n".join(lines[s + 1:e]).strip() or None
        return None

    contacts = {}
    em = re.search(r"[\w.+-]+@[\w-]+\.[\w.+-]+", text)
    if em:
        contacts["email"] = em.group()
    ph = re.search(r"(1[3-9]\d{9})", text)
    if ph:
        contacts["phone"] = ph.group()

    skills_raw = sec("skills")
    skills = []
    if skills_raw:
        skills = [s.strip().strip("-·").strip() for s in
                  re.split(r"[,;、/｜|·\s]{2,}", skills_raw) if s.strip() and len(s.strip()) > 1]

    yrs = None
    for pat in [r"(\d+)\s*年.*经验", r"工作经验[约]?(\d+)年"]:
        m = re.search(pat, text)
        if m:
            yrs = int(m.group(1))
            break

    return {"contact": contacts, "education": sec("education"), "experience": sec("experience"),
        "projects": sec("projects"), "skills": skills, "summary": sec("summary"),
        "years_experience": yrs, "raw": text}


def main():
    import argparse
    ap = argparse.ArgumentParser(description="简历解析")
    ap.add_argument("input")
    ap.add_argument("-o", "--output")
    args = ap.parse_args()
    t = args.input
    if os.path.isfile(args.input):
        with open(args.input, encoding="utf-8") as f:
            t = f.read()
    r = parse(t)
    o = json.dumps(r, ensure_ascii=False, indent=2)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(o)
        print(f"✅ 已保存至 {args.output}")
    else:
        print(o)


if __name__ == "__main__":
    main()
