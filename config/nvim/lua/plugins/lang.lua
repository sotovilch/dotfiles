return {
  -- Python
  {
    "hrsh7th/nvim-cmp",
    opts = function(_, opts)
      opts.auto_brackets = opts.auto_brackets or {}
      table.insert(opts.auto_brackets, "python")
    end,
  },

  {
    "linux-cultist/venv-selector.nvim",
    opts = function(_, opts)
      if LazyVim.has("nvim-dap-python") then
        opts.dap_enabled = true
      end
      return vim.tbl_deep_extend("force", opts, {
        name = {
          "venv",
          ".venv",
          "env",
          ".env",
          "env-*",
        },
      })
    end,
  },

  -- Typescript
  {
    "neovim/nvim-lspconfig",
    opts = {
      -- make sure mason installs the server
      servers = {
        tsserver = {
          enabled = false,
        },
        vtsls = {
          -- explicitly add default filetypes, so that we can extend
          -- them in related extras
          filetypes = {
            "javascript",
            "javascriptreact",
            "javascript.jsx",
            "typescript",
            "typescriptreact",
            "typescript.tsx",
          },
          settings = {
            complete_function_calls = true,
            vtsls = {
              enableMoveToFileCodeAction = true,
              autoUseWorkspaceTsdk = true,
              experimental = {
                completion = {
                  enableServerSideFuzzyMatch = true,
                },
              },
            },
            typescript = {
              updateImportsOnFileMove = { enabled = "always" },
              suggest = {
                completeFunctionCalls = true,
              },
              inlayHints = {
                enumMemberValues = { enabled = true },
                functionLikeReturnTypes = { enabled = true },
                parameterNames = { enabled = "literals" },
                parameterTypes = { enabled = true },
                propertyDeclarationTypes = { enabled = true },
                variableTypes = { enabled = false },
              },
            },
          },
          keys = {
            -- {
            --   "gD",
            --   function()
            --     local params = vim.lsp.util.make_position_params()
            --     LazyVim.lsp.execute({
            --       command = "typescript.goToSourceDefinition",
            --       arguments = { params.textDocument.uri, params.position },
            --       open = true,
            --     })
            --   end,
            --   desc = "Goto Source Definition",
            -- },
            -- {
            --   "gR",
            --   function()
            --     LazyVim.lsp.execute({
            --       command = "typescript.findAllFileReferences",
            --       arguments = { vim.uri_from_bufnr(0) },
            --       open = true,
            --     })
            --   end,
            --   desc = "File References",
            -- },
            {
              "<leader>co",
              "<cmd>TypescriptOrganizeImports<CR>",
              desc = "Organize Imports",
            },
            {
              "<leader>cM",
              "<cmd>TypescriptAddMissingImports<CR>",
              desc = "Add missing imports",
            },
            {
              "<leader>cu",
              "<cmd>TypescriptRemoveUnused<CR>",
              desc = "Remove unused imports",
            },
          },
        },
      },
      setup = {
        tsserver = function()
          -- disable tsserver
          return true
        end,
        vtsls = function(_, opts)
          -- copy typescript settings to javascript
          opts.settings.javascript =
            vim.tbl_deep_extend("force", {}, opts.settings.typescript, opts.settings.javascript or {})
        end,
      },
    },
  },

  {
    "williamboman/mason.nvim",
    opts = function(_, opts)
      opts.ensure_installed = opts.ensure_installed or {}
      table.insert(opts.ensure_installed, "js-debug-adapter")
    end,
  },
}
