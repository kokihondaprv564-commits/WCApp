<template>
  <div class="overlay" v-if="player">
    <div class="sheet">
      <header class="sheet-header">
        <div>
          <h3>{{ player.name }}</h3>
          <div class="sub">{{ player.club }} • {{ player.country }} • {{ player.position }}</div>
        </div>
        <button class="close" @click="$emit('close')">閉じる</button>
      </header>

      <div class="sheet-body">
        <div class="stats">
          <div class="stat"><span class="k">身長</span><span class="v">{{ player.height_cm }}cm</span></div>
          <div class="stat"><span class="k">年齢</span><span class="v">{{ player.age }}歳</span></div>
          <div class="stat"><span class="k">ゴール</span><span class="v">{{ player.goals }}</span></div>
          <div class="stat"><span class="k">アシスト</span><span class="v">{{ player.assists }}</span></div>
          <div class="stat"><span class="k">無失点試合</span><span class="v">{{ player.clean_sheets }}</span></div>
          <div class="stat"><span class="k">イエロー</span><span class="v">{{ player.yellow_cards }}</span></div>
          <div class="stat"><span class="k">レッド</span><span class="v">{{ player.red_cards }}</span></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Player } from '../services/playerService'

const props = defineProps<{ player: Player | null }>()
</script>

<style scoped>
.overlay { position: fixed; inset:0; background: rgba(2,6,23,0.6); display:flex; align-items:flex-end; justify-content:center; padding:1rem; z-index:50 }
.sheet { width:100%; max-width:720px; background:#fff; border-radius:12px 12px 6px 6px; overflow:hidden }
.sheet-header { display:flex; justify-content:space-between; align-items:center; padding:0.8rem 1rem; border-bottom:1px solid #eef2f6 }
.sheet-header h3 { margin:0 }
.sheet-body { display:flex; gap:1rem; padding:1rem }
.stats { display:grid; grid-template-columns: repeat(2,1fr); gap:0.6rem }
.stat { display:flex; justify-content:space-between; padding:0.6rem; background:#f8fafc; border-radius:8px }
.k { color:#475569 }
.v { font-weight:700 }
.close { background:#e2e8f0; border:none; padding:0.4rem 0.6rem; border-radius:8px }
@media(min-width:640px){ .overlay{align-items:center} }
</style>
