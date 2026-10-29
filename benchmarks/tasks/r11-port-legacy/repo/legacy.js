// Ported to lib.py: slugify, clamp, chunk. Not yet: parseRelative.

function slugify(s) { return s.toLowerCase().trim().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, ""); }
function clamp(x, lo, hi) { return Math.min(hi, Math.max(lo, x)); }
function chunk(xs, n) { const out = []; for (let i = 0; i < xs.length; i += n) out.push(xs.slice(i, i + n)); return out; }

const DAYS = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"];

// parseRelative("in 2 weeks", base) -> Date. Case-insensitive, surrounding spaces ignored.
// today | yesterday | tomorrow | N day(s)/week(s) ago | in N day(s)/week(s) |
// next <weekday> (strictly after base, 1-7 days) | last <weekday> (strictly before base, 1-7 days).
// Anything else throws Error("cannot parse: <text>").
function parseRelative(text, base) {
  const t = text.trim().toLowerCase();
  const day = 86400000;
  const add = (n) => new Date(base.getTime() + n * day);
  if (t === "today") return add(0);
  if (t === "yesterday") return add(-1);
  if (t === "tomorrow") return add(1);
  let m = t.match(/^(\d+) (day|week)s? ago$/);
  if (m) return add(-m[1] * (m[2] === "week" ? 7 : 1));
  m = t.match(/^in (\d+) (day|week)s?$/);
  if (m) return add(+m[1] * (m[2] === "week" ? 7 : 1));
  m = t.match(/^(next|last) (\w+)$/);
  if (m && DAYS.includes(m[2])) {
    const target = DAYS.indexOf(m[2]);
    const now = base.getUTCDay();
    if (m[1] === "next") return add(((target - now + 7) % 7) || 7);
    return add(-(((now - target + 7) % 7) || 7));
  }
  throw new Error("cannot parse: " + text);
}

module.exports = { slugify, clamp, chunk, parseRelative };
