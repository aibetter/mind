<script setup lang="ts">
import { useStorage } from '@/composables/useStorage'
import { useView } from '@/composables/useView'

defineOptions({
  name: 'LayoutHeader',
})

const { activeModelConfig } = useStorage()
const { toggleView } = useView()
</script>

<template>
  <header class="h-12 px-4 flex items-center text-base">
    <div class="flex items-center gap-2">
      <div class="cursor-pointer text-xl flex items-center justify-center" @click="toggleView('chat')">
        <i class="icon-[fluent-color--agents-48]" />
      </div>
      <div class="cursor-pointer" @click="toggleView('models')">
        {{ activeModelConfig.name }}
      </div>
    </div>
  </header>
</template>
