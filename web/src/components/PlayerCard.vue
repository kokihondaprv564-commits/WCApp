<template>
  <article class="player-card" @click="$emit('select', player)">
    <div class="main">
      <div class="name">{{ player.name }}</div>
      <div class="meta">{{ player.club }} • {{ player.country }}</div>
      <div class="badges">
        <span class="badge pos">{{ player.position }}</span>
        <span class="badge">{{ player.height_cm }}cm</span>
        <span class="badge">{{ player.age }}歳</span>
      </div>
    </div>
  </article>
</template>

<script setup lang="ts">
import type { Player } from '../services/playerService'

const props = defineProps<{ player: Player }>()
</script>

<style scoped>
.player-card {
  display: flex;
  gap: 0.75rem;
  padding: 0.75rem;
  border-radius: 8px;
  background: #fff;
  box-shadow: 0 1px 3px rgba(0,0,0,0.06);
  align-items: center;
  cursor: pointer;
  transition: transform .08s ease, box-shadow .12s ease;
}
.player-card:hover { transform: translateY(-2px); box-shadow: 0 6px 18px rgba(0,0,0,0.08); }
.player-card .name { font-weight:700; font-size:1rem }
.meta { color:#666; font-size:0.9rem }
.badges { margin-top:0.4rem; display:flex; gap:0.4rem }
.badge { background:#f1f5f9; color:#111827; padding:0.18rem 0.4rem; border-radius:999px; font-size:0.75rem }
.badge.pos { background:#e6f4ff; color:#0366d6 }
</style>
