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
{block name='customer_form'}
  {block name='customer_form_errors'}
    {include file='_partials/form-errors.tpl' errors=$errors['']}
  {/block}

  <form action="{block name='customer_form_actionurl'}{$action}{/block}" id="customer-form" class="js-customer-form"
    method="post">
    <div>
      <div class="form-group row ">
        <label class="col-md-3 form-control-label required" for="field-firstname">
          Imię
        </label>
        <div class="col-md-6">
          <input id="field-firstname" class="form-control" name="firstname" type="text" value="" required="">
          <span class="form-control-comment">
            Tylko litery, kropka (.) i spacja są dozwolone.
          </span>
        </div>
        <div class="col-md-3 form-control-comment"></div>
      </div>
      <div class="form-group row ">
        <label class="col-md-3 form-control-label required" for="field-lastname">
          Nazwisko
        </label>
        <div class="col-md-6">
          <input id="field-lastname" class="form-control" name="lastname" type="text" value="" required="">
          <span class="form-control-comment">
            Tylko litery, kropka (.) i spacja są dozwolone.
          </span>
        </div>
        <div class="col-md-3 form-control-comment"></div>
      </div>
      <div class="form-group row ">
        <label class="col-md-3 form-control-label required" for="field-email">
          E-mail
        </label>
        <div class="col-md-6">
          <input id="field-email" class="form-control" name="email" type="email" value="" required="">
        </div>
        <div class="col-md-3 form-control-comment"></div>
      </div>
      <div class="form-group row ">
        <label class="col-md-3 form-control-label required" for="field-password">
          Hasło
        </label>
        <div class="col-md-6">
          <div class="input-group js-parent-focus">
            {literal}
              <input id="field-password" class="form-control js-child-focus js-visible-password" name="password"
                title="Co najmniej 5 znaków" aria-label="Hasło musi zawierać przynajmniej 5 znaków" type="password" value=""
                pattern=".{5,}" required="">
            {/literal}
            <span class="input-group-btn">
              <button class="btn" type="button" data-action="show-password" data-text-show="Pokaż" data-text-hide="Ukryj">
                Pokaż
              </button>
            </span>
          </div>
        </div>
        <div class="col-md-3 form-control-comment"></div>
      </div>
      <div class="form-group row ">
        <label class="col-md-3 form-control-label required" for="field-agreement_1">
        </label>
        <div class="col-md-6">
          <span class="custom-checkbox">
            <label>
              <input name="customer_privacy" type="checkbox" value="1" required="">
              <span><i class="material-icons rtl-no-flip checkbox-checked"></i></span>
              Niniejszym wyrażam zgodę na przetwarzanie moich danych osobowych przez Orzełek.it z siedzibą w Kłobuck
              (42-100) przy ul. Wojska Polskiego 15, zarejestrowaną w Kłobuck, nr NIP: 5741882651, nr REGON: 385285808 na
              potrzeby i w zakresie niezbędnym do korzystania przeze mnie z usług świadczonych przez Orzełek.it, w tym na
              przekazywanie moich danych osobowych podmiotom trzecim, przy pomocy których Orzełek.it świadczy usługi
              związane z realizacją zamówień oraz obsługą płatności.
            </label>
          </span>
          <div class="help-block" style="display: none;">
            <ul>
              <li class="alert alert-danger">- pole wymagane</li>
            </ul>
          </div>
        </div>
        <div class="col-md-3 form-control-comment"></div>
      </div>
      <input type="hidden" name="captcha" value="1">
      <div class="captcha_register form-group row required register page_authentication ver17">
        <label for="pa_captcha" class="col-md-3"></label>
        <div class="pa-captcha-inf col-md-6">
          <div id="g-recaptcha-response-476878732">
            <div class="grecaptcha-badge" data-style="bottomright"
              style="width: 256px; height: 60px; display: block; transition: right 0.3s; position: fixed; bottom: 14px; right: -186px; box-shadow: gray 0px 0px 5px; border-radius: 2px; overflow: hidden;">
              <div class="grecaptcha-logo"><iframe title="reCAPTCHA" width="256" height="60" role="presentation"
                  name="a-oqz28q99582" frameborder="0" scrolling="no"
                  sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox allow-storage-access-by-user-activation"
                  src="https://www.google.com/recaptcha/api2/anchor?ar=1&amp;k=6LflricpAAAAADYbQ4B9YYxJBGyd4uDUoduganf0&amp;co=aHR0cHM6Ly9tb25vY2VydXMucGw6NDQz&amp;hl=pl&amp;v=TkacYOdEJbdB_JjX802TMer9&amp;theme=light&amp;size=invisible&amp;badge=bottomright&amp;anchor-ms=20000&amp;execute-ms=15000&amp;cb=9a7eringia5e"></iframe>
              </div>
              <div class="grecaptcha-error"></div><textarea id="g-recaptcha-response" name="g-recaptcha-response"
                class="g-recaptcha-response"
                style="width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none; display: none;"></textarea>
            </div><iframe style="display: none;"></iframe><input type="hidden" name="g-recaptcha-response"
              value="0cAFcWeA55GY0UPgL6vNhDhXyMnMM4_stcbnT1h1PRBeWmNkOC9PeixoW4MoqHlEN_-D-lKeh8o_QNfITy0Dcx1VSbHEJl9pJR3VItOGQTTCkAzmdGorDdcboogg4JAJXcCqG0ElNHOfk86DzA6ivjbtxVXuWGnk8C8iikJqQJU0BpDaafpl74Fhkh7_mmKZ0W9uRrXDLpUO9MZoaacys7RXQgvD8l7mcXu0LlFn60oXen3VCYDAr7K07feMhHeFd6tksFTpc8an1Up2Ab1FgTnDeJs9qzZaKuQf1TPKNzBzthNww9_ZqGDvriTfLcoA-VJbFuGHwS_TI8RdbMSNftpTcFbzEaABJm2IhH4eqjNjQJ27xIWn389tiUSrkciG4Ngmut6DN1qzXNVDVdixpEwApWOvSla0FkjT_X4fWWW7CaHYjF94bkRY2MkYTrWV3OPi_bLYQRPecwr5eNko92pDVobWFNABLUViMb2GUixRBjKFj6yJwdXuEUWxn7K4tO9kMTOtGDO5ECFOGR4m-EU5h3vqU89KAm6DQubU-RiJQvslJYcfmikC8DkIUjt3ZCWldWoYEe4lMZVNQAv_DOIj0axCv2M5zpLCHRe60SvtbWRMm5NcuSDpaJXz9eFwHfjd8orY0vWiqAGpYsDUs5qrBLdRCA_T1FzyJaPkYAXnu_FFJePcZruBLqtWA73j2rjCmAeix1b258v9YTv9MRoaGUWmdDN0WxbMOTlokQCSyNY4jMj3H_A9AZVTE2JdJbl4SSIBEmHfoaV8Uf4y5_WY4eG8FZvTe4ib5kzLTKiWrF3xmall096ptGoJRhvcRJF1r2FJpG-ay_k0SOhr3-8aT0LO0By3csajBMfGEt5USW7VZQBPg9plL-R2iLY4IE75MX_zhIyMxh14lbm-5pCLJVbVbI7NAwDtZEUvA-a5NRc1XhVU1zjTzuFstc1km1UREekdW_DzZkFgYj_mtMDbaICLc_2IQgA5YZc0kmZJoyJV1N_-0iAaoFD-BdqybCO_5UARTCRNNiHa9vMbjJ6zhKWxJJSZwqqlbmZpKhZXwu9JCv4q5O27iPSZhgjmg9Tz0bhmBMOmmQf8FiLaFzPbxxigUBZFNVSi6R3RS3HkOckosK1h1C3acHFKxLHwE4mZsuN1Z3MYrOQVBbS_OHSKe_uTimQ2D69nRuiZl4AXkPzmj3UMEBnty1A7ONoUe9pSEoFny1pRZnLdf6Mq2Rmlcm4WS3EKEyXAZ6KNWoZy3tpJi2h2x0PWgYxLrdqE-Iv3eP1zBL3hrmJjy6yhaZuvsuq0q35QlmRPiBLXqkXyAsOnwnuHwMZBaDuYHKP0RTpNWgvf0JLgc1__A-NZtOfCk8IGZqWKYZxXjqYiU0ZnEV3pzeDvTiYxHyLwN7zZx6YVQ8z-30Bezbz1EXveppHnlOK4cpDcfil87t6700nM-F52h4slmmQZaw_rQ1-Ar-aBDd7IEW4_36CspNctYWDDagsvR1Gb7oLVkYszQdIsMuU6dFL6MXdZ16unIzs7rK375CPuceVEfSbxOyBx7rQt0am1y258mngsSoVkiOf61BU4dr_pAcbVngFwc8bpYvSUiDqP7aUwiKWMVj8xq6VtEXw2IWxgaHSq4e77b43MGGdCS9gYm-rmE">
          </div>
        </div>
        <div class="col-md-3 form-control-comment"></div>
      </div>
      <div class="col-md-6" style="display: none;">
        <span class="custom-checkbox">
          <label>
            <input name="psgdpr" type="checkbox" value="1" required="" checked>
            <span><i class="material-icons rtl-no-flip checkbox-checked"></i></span>
            Akceptuję ogólne warunki użytkowania i politykę prywatności
          </label>
        </span>
        <div class="help-block">
          <ul>
            <li class="alert alert-danger">- pole wymagane</li>
          </ul>
        </div>
      </div>
      {include file='catalog/_partials/google_button.tpl'}
    </div>

    {block name='customer_form_footer'}
      <footer class="form-footer clearfix">
        <input type="hidden" name="submitCreate" value="1">
        {block "form_buttons"}
          <button class="btn btn-primary form-control-submit float-xs-right" data-link-action="save-customer" type="submit">
            {l s='Save' d='Shop.Theme.Actions'}
          </button>
        {/block}
      </footer>
    {/block}

  </form>
{/block}