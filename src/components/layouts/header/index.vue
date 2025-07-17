<script setup lang="ts">
import { useStorage } from '@/composables/useStorage'

defineOptions({
  name: 'LayoutHeader',
})

const { activeModelConfig } = useStorage()
</script>

<template>
  <header class="h-12 px-4 flex items-center">
    <div>
      {{ activeModelConfig.name }}
    </div>
  </header>
</template>
