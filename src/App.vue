<script setup lang="ts">
import LayoutBody from '@/components/layouts/Body.vue'
import LayoutHeader from '@/components/layouts/header/index.vue'
import { useStorage } from '@/composables/useStorage'
import ViewModels from '@/views/models/index.vue'

defineOptions({
  name: 'MindApp',
})

useStorage()
</script>

<template>
  <div class="bg-white text-neutral-900">
    <LayoutHeader />
    <LayoutBody class="h-[calc(100vh-3rem)] overflow-auto">
      <ViewModels />
    </LayoutBody>
  </div>
</template>
