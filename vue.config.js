const { defineConfig } = require('@vue/cli-service')
const path = require('path')

module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave: true,
  configureWebpack: {
    entry: './vueClient/src/main.ts',
  },
  outputDir: path.resolve(__dirname, './static/vue/'),
  filenameHashing: false,
  runtimeCompiler: true,
  devServer: {
    static: true,
  }
})
