const STORAGE_KEY = "ghost-history", TIMEOUT = 864e5, LIMIT = 15;
!async function () {
    try {
        const e = window.localStorage, r = e.getItem(STORAGE_KEY), t = (new Date).getTime();
        let i = [];
        if (r) try {
            i = JSON.parse(r)
        } catch (e) {
            console.warn("[Member Attribution] Error while parsing history", e)
        }
        const n = i.findIndex((e => {
            if (!e.time || "number" != typeof e.time) return !1;
            const r = t - e.time;
            return !(isNaN(e.time) || r > TIMEOUT)
        }));
        let o, a, s, c;
        n > 0 ? i.splice(0, n) : -1 === n && (i = []);
        try {
            const e = new URL(window.location.href);
            o = e.searchParams.get("ref"), a = e.searchParams.get("source"), s = e.searchParams.get("utm_source"), c = e.searchParams.get("utm_medium")
        } catch (e) {
            console.error("[Member Attribution] Parsing referrer from querystring failed", e)
        }
        const l = o || a || s || null, h = c || null, u = window.document.referrer || null;
        try {
            const e = new URL(window.location.href), r = e.searchParams;
            r.get("attribution_id") && r.get("attribution_type") && (i.push({
                time: t,
                id: r.get("attribution_id"),
                type: r.get("attribution_type"),
                referrerSource: l,
                referrerMedium: h,
                referrerUrl: u
            }), r.delete("attribution_id"), r.delete("attribution_type"), e.search = "?" + r.toString(), window.history.replaceState({}, "", `${e.pathname}${e.search}${e.hash}`))
        } catch (e) {
            console.error("[Member Attribution] Parsing attribution from querystring failed", e)
        }
        const m = window.location.pathname;
        0 === i.length || i[i.length - 1].path !== m ? i.push({
            path: m,
            time: t,
            referrerSource: l,
            referrerMedium: h,
            referrerUrl: u
        }) : i.length > 0 && (i[i.length - 1].time = t, l && (i[i.length - 1].referrerSource = l, i[i.length - 1].referrerMedium = h), u && (i[i.length - 1].referrerUrl = u)), i.length > 15 && (i = i.slice(-15)), e.setItem(STORAGE_KEY, JSON.stringify(i))
    } catch (e) {
        console.error("[Member Attribution] Failed with error", e)
    }
}();