<script setup lang="ts">
import { fetch } from '@tauri-apps/plugin-http'
import { computed, ref, shallowRef } from 'vue'
import { useStorage } from '@/composables/useStorage'

interface RemoteModel {
  id: string
  name: string
  description: string
  context_length: number
}

const remoteModels = shallowRef<RemoteModel[]>([])
const remoteModelsLoading = ref(true)
fetch('https://openrouter.ai/api/v1/models?max_price=0')
  .then(res => res.json())
  .then((data) => {
    remoteModels.value = data.data
  })
  .finally(() => {
    remoteModelsLoading.value = false
  })

const searchKey = ref('')
const filterRemoteModels = computed(() => {
  return remoteModels.value?.filter(model => model.name.toLowerCase().includes(searchKey.value.toLowerCase())) ?? []
})

const { activeModelConfig } = useStorage()
function onSelectModel(model: RemoteModel) {
  activeModelConfig.value = {
    name: model.name,
    id: model.id,
    provider: 'remote',
  }
}
</script>

<template>
  <div class="p-4 flex flex-col gap-6">
    <div class="flex items-center gap-2 border border-solid border-gray-300 rounded-lg focus-within:border-blue-500 p-2">
      <i class="icon-[material-symbols--search-rounded] text-xl" />
      <input v-model="searchKey" class="focus:outline-none" placeholder="Search model by name">
    </div>
    <div class="grid grid-cols-3 gap-4">
      <div
        v-for="model in filterRemoteModels"
        :key="model.id"
        class="p-3 rounded-xl border border-solid border-gray-300 cursor-pointer flex flex-col gap-1 transition-colors hover:bg-gray-100"
        :class="{
          '!bg-blue-100 !cursor-default': model.id === activeModelConfig.id,
        }"
        @click="onSelectModel(model)"
      >
        <div class="text-sm font-medium">
          {{ model.name }}
        </div>
        <div class="line-clamp-2 text-xs text-neutral-700">
          {{ model.description }}
        </div>
        <div>
          <span class="text-xs py-1 px-2 rounded-md bg-gray-50 border border-solid border-gray-200">
            {{ Math.floor(model.context_length / 1000) }}K context
          </span>
        </div>
      </div>
    </div>
  </div>
</template>
