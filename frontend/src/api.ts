export async function apiJson<T = any>(url: string, init: RequestInit = {}) {
  const res = await fetch(url, { ...init, credentials: "include" });
  if (!res.ok) throw new Error(`${res.status} ${res.statusText}`);
  return res.json() as Promise<T>;
}

export type ElementDetails = {
  atomic_number: number;
  symbol: string;
  name: string;
  last_ts: string | null;
  last_price?: string | null;
};

export function getElementData(symbol: string) {
  // DRF uses trailing slash
  return apiJson<ElementDetails>(`/api/elements/${symbol}/`);
}

// Add more API

function getCookie(name: string | undefined): string {
  if (!name) return "";
  const m = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
  return m ? decodeURIComponent(m.pop() as string) : "";
}

export async function initApi() {
  await fetch("/api/csrf/", { credentials: "include" });
}

export async function api<T>(url: string, init: RequestInit = {}): Promise<T> {
  const method = (init.method || "GET").toUpperCase();
  const headers = new Headers(init.headers || {});
  if (method !== "GET" && !headers.has("X-CSRFToken")) {
    headers.set("X-CSRFToken", getCookie("csrftoken"));     // read cookie → header
    if (!headers.has("Content-Type")) headers.set("Content-Type", "application/json");
  }
  const res = await fetch(url, { ...init, headers, credentials: "include" });
  if (!res.ok) throw new Error(`${res.status} ${res.statusText}`);
  return res.json() as Promise<T>;
}