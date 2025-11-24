{assign var=_counter value=0}
{function name="menu" nodes=[] depth=0 parent=null}
  {if $nodes|count}
    <ul class="top-menu" {if $depth == 0}id="top-menu" {/if} data-depth="{$depth}">
      {if $depth == 0}
        <li class="category" id="index-page">
          <a class="dropdown-item" href="{$urls.base_url}" data-depth="{$depth}">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 1664 1664">
              <g transform="translate(0,1664) scale(1,-1)">
                <path
                  d="M1408 544v-480q0 -26 -19 -45t-45 -19h-384v384h-256v-384h-384q-26 0 -45 19t-19 45v480q0 1 0.5 3t0.5 3l575 474l575 -474q1 -2 1 -6zM1631 613l-62 -74q-8 -9 -21 -11h-3q-13 0 -21 7l-692 577l-692 -577q-12 -8 -24 -7q-13 2 -21 11l-62 74q-8 10 -7 23.5t11 21.5 l719 599q32 26 76 26t76 -26l244 -204v195q0 14 9 23t23 9h192q14 0 23 -9t9 -23v-408l219 -182q10 -8 11 -21.5t-7 -23.5z" />
              </g>
            </svg>
            Strona główna
          </a>
        </li>
        <li class="category">
          <a class="dropdown-item" href="{$urls.base_url}pl/promocje" data-depth="{$depth}">
            Promocje
          </a>
        </li>
        <li class="category">
          <a class="dropdown-item" href="{$urls.base_url}" data-depth="{$depth}">
            Producenci
            <svg class="tri-desc" viewBox="0 0 14 13" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="tri-desc"
              width=14 height=13>
              <title id="tri-desc">Strzałka w dół</title>
              <path d="M0 0 L14 0 L7 13 Z" fill="#484848" />
            </svg>
          </a>
          <div {if $depth === 0} class="popover sub-menu js-sub-menu collapse" {else} class="collapse" {/if}
            id="top_sub_menu_0">
            <ul class="top-menu" data-depth="{$depth + 1}">
            {/if}
            {foreach from=$nodes item=node}
              <li class="{$node.type}{if $node.current} current {/if} submenu" id="{$node.page_identifier}">
                {assign var=_counter value=$_counter+1}
                <a class="{if $depth >= 0}dropdown-item{/if}" href="{$node.url}" data-depth="{$depth + 1}"
                  {if $node.open_in_new_window} target="_blank" {/if}>
                  {if $node.children|count}
                    {* Cannot use page identifier as we can have the same page several times *}
                    {assign var=_expand_id value=10|mt_rand:100000}
                    <span class="float-xs-right hidden-md-up">
                      <span data-target="#top_sub_menu_{$_expand_id}" data-toggle="collapse"
                        class="navbar-toggler collapse-icons">
                        <i class="material-icons add">&#xE313;</i>
                        <i class="material-icons remove">&#xE316;</i>
                      </span>
                    </span>
                  {/if}
                  {$node.label}

                </a>

              </li>
            {/foreach}
            {if $depth == 0}
            </ul>
          </div>
        </li>
        <li class="category">
          <a class="dropdown-item" href="{$urls.base_url}pl/outlet" data-depth="{$depth}">
            Outlet
          </a>
        </li>
        <li class="category">
          <a class="dropdown-item" href="https://news.monocerus.pl/" data-depth="{$depth}">
            Monocerus News
          </a>
        </li>
      {/if}
    </ul>
  {/if}
{/function}

<div class="menu js-top-menu position-static hidden-sm-down" id="_desktop_top_menu">
  {menu nodes=$menu.children}
  <div class="clearfix"></div>
</div>