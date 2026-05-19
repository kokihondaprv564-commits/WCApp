<template>
  <section class="players-shell">
    <header class="topbar">
      <h2>選手一覧</h2>
      <div class="search-row">
        <input v-model="quick" @keyup.enter="onQuickSearch" placeholder="選手名やクラブで検索（Enterで実行）" class="quick-input" />
        <button @click="showAdvanced = !showAdvanced" class="btn">詳細</button>
        <button @click="onSearch" class="btn primary">検索</button>
      </div>
      <div v-if="showAdvanced" class="advanced">
        <form @submit.prevent="onSearch" class="search-form">
          <input v-model="filters.name" placeholder="名前（部分一致）" />
          <input v-model="filters.club" placeholder="所属クラブ（部分一致）" />
          <input v-model="filters.country" placeholder="国（完全一致）" />
          <select v-model="filters.position">
            <option value="">全てのポジション</option>
            <option value="GK">GK</option>
            <option value="DF">DF</option>
            <option value="MF">MF</option>
            <option value="FW">FW</option>
          </select>
          <input type="number" v-model.number="filters.min_height" placeholder="最小身長(cm)" />
          <input type="number" v-model.number="filters.max_height" placeholder="最大身長(cm)" />
          <input type="number" v-model.number="filters.min_age" placeholder="最小年齢" />
          <input type="number" v-model.number="filters.max_age" placeholder="最大年齢" />
        </form>
      </div>
    </header>

    <p v-if="loading" class="loading">ロード中…</p>
    <p v-if="error" class="error">{{ error }}</p>

    <div class="grid">
      <PlayerCard v-for="p in players" :key="p.id" :player="p" @select="openPlayer" />
    </div>

    <p v-if="total !== null" class="total">合計：{{ total }}</p>

    <PlayerDetail :player="selectedPlayer" v-if="showDetail" @close="closeDetail" />
  </section>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { searchPlayers, Player, PlayerQueryParams } from '../services/playerService'
import PlayerCard from './PlayerCard.vue'
import PlayerDetail from './PlayerDetail.vue'

type Filters = PlayerQueryParams & { name?: string; country?: string; position?: string }

const players = ref<Player[]>([])
const total = ref<number | null>(null)
const loading = ref(false)
const error = ref<string | null>(null)

const filters = ref<Filters>({
  name: '',
  club: '',
  country: '',
  position: '',
  min_height: undefined,
  max_height: undefined,
  min_age: undefined,
  max_age: undefined,
})

const quick = ref('')
const showAdvanced = ref(false)
const selectedPlayer = ref<Player | null>(null)
const showDetail = ref(false)

async function fetchWithFilters(params: PlayerQueryParams) {
  loading.value = true
  error.value = null
  try {
    const res = await searchPlayers(params)
    players.value = res.players
    total.value = res.total
  } catch (e: unknown) {
    error.value = e instanceof Error ? e.message : String(e)
  } finally {
    loading.value = false
  }
}

function buildQueryFromFilters(f: Filters): PlayerQueryParams {
  const out: PlayerQueryParams = {}
  if (f.name && f.name.trim() !== '') out.name = f.name.trim()
  if (f.country && f.country.trim() !== '') out.country = f.country.trim()
  if (f.position && f.position.trim() !== '') out.position = f.position.trim()
  if (f.club && f.club.trim() !== '') out.club = f.club.trim()
  if (typeof f.min_height === 'number' && !Number.isNaN(f.min_height)) out.min_height = f.min_height
  if (typeof f.max_height === 'number' && !Number.isNaN(f.max_height)) out.max_height = f.max_height
  if (typeof f.min_age === 'number' && !Number.isNaN(f.min_age)) out.min_age = f.min_age
  if (typeof f.max_age === 'number' && !Number.isNaN(f.max_age)) out.max_age = f.max_age
  return out
}

async function onSearch() {
  const params = buildQueryFromFilters(filters.value)
  await fetchWithFilters(params)
}

function onQuickSearch() {
  filters.value.name = quick.value
  onSearch()
}

function openPlayer(player: Player) {
  selectedPlayer.value = player
  showDetail.value = true
}

function closeDetail() {
  showDetail.value = false
  selectedPlayer.value = null
}

onMounted(() => {
  // 初期表示で全件取得（空フィルタ）
  onSearch()
})
</script>

<style scoped>
.search-form {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1rem;
}
.search-form input,
.search-form select {
  padding: 0.4rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}
</style>
