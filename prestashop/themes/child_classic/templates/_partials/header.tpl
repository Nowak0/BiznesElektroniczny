{**
 * Copyright since 2007 PrestaShop SA and Contributors
 * PrestaShop is an International Registered Trademark & Property of PrestaShop SA
 *
 * NOTICE OF LICENSE
 *
 * This source file is subject to the Academic Free License 3.0 (AFL-3.0)
 * that is bundled with this package in the file LICENSE.md.
 * It is also available through the world-wide-web at this URL:
 * https://opensource.org/licenses/AFL-3.0
 * If you did not receive a copy of the license and are unable to
 * obtain it through the world-wide-web, please send an email
 * to license@prestashop.com so we can send you a copy immediately.
 *
 * DISCLAIMER
 *
 * Do not edit or add to this file if you wish to upgrade PrestaShop to newer
 * versions in the future. If you wish to customize PrestaShop for your
 * needs please refer to https://devdocs.prestashop.com/ for more information.
 *
 * @author    PrestaShop SA and Contributors <contact@prestashop.com>
 * @copyright Since 2007 PrestaShop SA and Contributors
 * @license   https://opensource.org/licenses/AFL-3.0 Academic Free License 3.0 (AFL-3.0)
 *}
{block name='header_banner'}
  <div class="header-banner">
    {hook h='displayBanner'}
  </div>
{/block}

{block name='header_nav'}
  <nav class="header-nav">
    <div class="container">
      <div class="row">
        <div class="hidden-sm-down">
          <div class="col-md-5 col-xs-12">
            {hook h='displayNav1'}
          </div>
          <div class="col-md-7 right-nav">
              {hook h='displayNav2'}
          </div>
        </div>
        <div class="hidden-md-up text-sm-center mobile">
          <div class="float-xs-left" id="menu-icon">
            <i class="material-icons d-inline">&#xE5D2;</i>
          </div>
          <div class="float-xs-right" id="_mobile_cart"></div>
          <div class="float-xs-right" id="_mobile_user_info"></div>
          <div class="top-logo" id="_mobile_logo"></div>
          <div class="clearfix"></div>
        </div>
      </div>
    </div>
  </nav>
{/block}

{block name='header_top'}
  <div class="header-top">
    <div class="container">
       <div class="row">
        <div class="col-md-2 hidden-sm-down" id="_desktop_logo">
          {if $shop.logo_details}
            {if $page.page_name == 'index'}
              <h1>
                <a href="{$urls.base_url}">
                  {renderLogo}
                </a>
              </h1>
            {else}
              <a href="{$urls.base_url}">
                {renderLogo}
              </a>
            {/if}
          {/if}
        </div>
        <div class="header-top-right col-md-10 col-sm-12 position-static">
          {hook h='displayTop'}
          
          {include file='catalog/_partials/google_button.tpl'}
          
        </div>
      </div>
      <div id="mobile_top_menu_wrapper" class="row hidden-md-up" style="display:none;">
        <div class="js-top-menu mobile" id="_mobile_top_menu"></div>
        <div class="js-top-menu-bottom">
          <div id="_mobile_currency_selector"></div>
          <div id="_mobile_language_selector"></div>
          <div id="_mobile_contact_link"></div>
        </div>
      </div>
    </div>
  </div>
  {hook h='displayNavFullWidth'}
{/block}

{block name='header_top'}
  <div class="ets_mm_megamenu layout_layout1 show_icon_in_mobile transition_fade transition_floating sticky_enabled ets-dir-ltr hook-default single_layout disable_sticky_mobile hover mm_menu_left" data-bggray="bg_gray" id="main_menu">
    <div class="ets_mm_megamenu_content">
      <div class="container">
        <div class="ets_mm_megamenu_content_content">
          <div class="ybc-menu-toggle ybc-menu-btn closed">
            <span class="ybc-menu-button-toggle_icon">
              <i class="icon-bar"></i>
              <i class="icon-bar"></i>
              <i class="icon-bar"></i>
            </span>
            Menu
          </div>
                        
          {hook h='displayMenu'}

          <script type="text/javascript">
              var Days_text = 'Dni';
              var Hours_text = 'Godz.';
              var Mins_text = 'Min.(y)';
              var Sec_text = 'Sek(s)';

              let navbar = document.getElementById("main_menu");
              let navPos = navbar.getBoundingClientRect().top;

              window.addEventListener("scroll", e => {
                let viewportHeight = window.innerHeight;
                let scrollPos = window.scrollY;
                if (scrollPos > navPos) {
                  navbar.classList.add('sticky');
                  header.classList.add('navbarOffsetMargin');
                } else {
                  navbar.classList.remove('sticky');
                  header.classList.remove('navbarOffsetMargin');
                }
              });
          </script>    
          <style>
            #main_menu.sticky {
              position: fixed;
              top: 0;
              width: 100%;
            }
            .navbarOffsetMargin {
              padding-top: 45px;
            }
          </style>

          <div class="mm_extra_item">
            {hook h='displayShoppingcart'}
          </div>

        </div>
      </div>
    </div>
  </div>
{/block}
