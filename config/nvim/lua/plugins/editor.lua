return {
  {
    "nvim-neo-tree/neo-tree.nvim",
    opts = {
      filesystem = {
        filtered_items = {
          visible = true,
          hide_dotfiles = false,
          hide_gitignored = true,
          hide_by_name = {
            ".DS_Store",
            "thumbs.db",
            "node_modules",
            "package-lock.json",
          },
          never_show = {
            ".git",
          },
        },
      },
    },
  },
}
