<script setup lang="ts">
import { computed, markRaw } from 'vue'
import LayoutBody from '@/components/layouts/Body.vue'
import LayoutHeader from '@/components/layouts/header/index.vue'
import { useStorage } from '@/composables/useStorage'
import { useView } from '@/composables/useView'
import ViewChat from '@/views/chat/index.vue'
import ViewModels from '@/views/models/index.vue'

defineOptions({
  name: 'MindApp',
})

useStorage()

const { activeView } = useView()
const activeViewComponent = computed(() => {
  if (activeView.value === 'models') {
    return markRaw(ViewModels)
  }

  return markRaw(ViewChat)
})
</script>

<template>
  <div class="bg-white text-neutral-900">
    <LayoutHeader />
    <LayoutBody class="h-[calc(100vh-3rem)] overflow-auto">
      <component :is="activeViewComponent" />
    </LayoutBody>
  </div>
</template>
