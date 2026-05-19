<template>
  <section>
    <h2>Players</h2>
    <ul>
      <li v-for="p in players" :key="p.id">{{ p.name }} — {{ p.country }} ({{ p.position }})</li>
    </ul>
  </section>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'

const players = ref<any[]>([])

onMounted(async () => {
  try {
    const res = await fetch('http://localhost:8000/players')
    players.value = await res.json()
  } catch (e) {
    console.error(e)
  }
})
</script>
