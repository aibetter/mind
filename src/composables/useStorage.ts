import { Store } from '@tauri-apps/plugin-store'
import { createSharedComposable } from '@vueuse/core'
import { ref, shallowRef, watch } from 'vue'

interface ActiveModelConfig {
  name: string
  id: string
  provider: 'remote' | 'local'
}

export const useStorage = createSharedComposable(() => {
  const store = shallowRef<Store>()

  const activeModelConfig = ref<Partial<ActiveModelConfig>>({})
  watch(activeModelConfig, (newVal) => {
    store.value?.set('activeModelConfig', newVal)
  }, {
    deep: true,
  })

  Store.load('model.json', {
    autoSave: true,
  }).then((_store) => {
    store.value = _store

    store.value?.get('activeModelConfig').then((value) => {
      activeModelConfig.value = value ?? {
        name: undefined,
        id: undefined,
        provider: undefined,
      }
    })
  })

  return {
    activeModelConfig,
  }
})
