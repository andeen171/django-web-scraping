<template>
  <div class="container max-w-md m-auto">
    <div class="flex justify-center space-x-2">
      <input
        v-model="input"
        @change="searchProducts"
        type="text"
        placeholder="Busca"
        name="term"
        class="border-2 p-2 rounded"
      />
      <select @change="searchProducts" class="border-2 rounded" name="limit" v-model="limit">
        <option value="5">5</option>
        <option value="10">10</option>
        <option value="20">20</option>
        <option value="50">50</option>
      </select>
    </div>
    <CodeIcon v-if="loading" class="h-10 w-10 m-auto mt-5 animate-pulse text-blue-500 " />
    <div class="m-5 p-2 rounded-xl shadow-2xl" v-for="product in products">
      <p class="text-blue-500 font-semibold">{{ product.name }}</p>
      <a target="_blank" :href="product.urlKey">
        <img alt="product-image" :src="product.thumbnail" />
      </a>
      <p>Marca: {{ product.brand }}</p>
      <p>Quantidade em estoque: {{ product.qtyInStock }}</p>
      <p>Preço: R${{ product.valueFrom }} - R${{ product.valueTo }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { CodeIcon } from '@heroicons/vue/solid'

export default {
  name: 'SearchBar',
  components: { CodeIcon },
  data() {
    return {
      input: '',
      products: [],
      limit: 10,
      loading: false,
    }
  },
  methods: {
    async searchProducts() {
      this.loading = true
      await axios
        .get(
          'http://localhost:8000/api/search?term=' +
            this.input +
            '&limit=' +
            this.limit
        )
        .then((response) => {
          this.products = response.data
        })
        .finally(() => {
          this.loading = false
        })
    },
  },
}
</script>

<style scoped>
img {
  height: 100px;
  width: auto;
  margin: auto;
}
</style>
