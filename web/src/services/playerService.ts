export type Player = {
  id: number
  name: string
  country: string
  club: string
  position: string
  height_cm: number
  age: number
}

export type PlayerListResponse = {
  players: Player[]
  total: number
}

export type PlayerQueryParams = Partial<{
  name: string
  country: string
  club: string
  position: string
  min_height: number
  max_height: number
  min_age: number
  max_age: number
  offset: number
  limit: number
}>

export async function searchPlayers(params: PlayerQueryParams): Promise<PlayerListResponse> {
  const url = new URL('http://127.0.0.1:8080/players')
  Object.entries(params ?? {}).forEach(([k, v]) => {
    if (v !== undefined && v !== null && v !== '') {
      url.searchParams.append(k, String(v))
    }
  })

  const res = await fetch(url.toString())
  if (!res.ok) {
    const text = await res.text()
    throw new Error(text || `HTTP ${res.status}`)
  }
  return res.json()
}
