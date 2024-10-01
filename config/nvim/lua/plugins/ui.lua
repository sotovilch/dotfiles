return {
  {
    "nvimdev/dashboard-nvim",
    opts = function(_, opts)
      local logo = [[
 ██████╗ ███████╗██████╗ ███████╗ ██████╗ ████████╗ ██████╗ 
██╔════╝ ██╔════╝██╔══██╗██╔════╝██╔═══██╗╚══██╔══╝██╔═══██╗
██║  ███╗█████╗  ██████╔╝███████╗██║   ██║   ██║   ██║   ██║
██║   ██║██╔══╝  ██╔══██╗╚════██║██║   ██║   ██║   ██║   ██║
╚██████╔╝███████╗██║  ██║███████║╚██████╔╝   ██║   ╚██████╔╝
 ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝    ╚═╝    ╚═════╝ 
    ]]

      logo = string.rep("\n", 8) .. logo .. "\n\n"
      opts.config.header = vim.split(logo, "\n")
    end,
  },

  -- the opts function can also be used to change the default opts:
  {
    "nvim-lualine/lualine.nvim",
    event = "VeryLazy",
    opts = function(_, opts)
      table.insert(opts.sections.lualine_x, "😄")
    end,
  },
}
