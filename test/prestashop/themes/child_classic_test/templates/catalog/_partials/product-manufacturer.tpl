{if $product_manufacturer->name eq "Reeves International, Inc."}
    <span>Reeves International, Inc.</span>
    <span>Industrial Road 14</span>
    <span>NJ 07440 Pequannock</span>
    <span>Stany Zjednoczone</span>
    <span><a href="mailto:info@reevesintl.com">info@reevesintl.com</a></span>
{elseif $product_manufacturer->name eq "Mojo"}
    <span>Mojo</span>
    <span>King’s Road 338</span>
    <span>North Point North Point, Hongkong</span>
    <span>SRA Hongkong (Chiny)</span>
    <span class="x13gpsr__item"><a href="mailto:info@mojofun.eu">info@mojofun.eu</a></span>
{else}
    {foreach from=$product_manufacturer key=key item=value}
        <strong>{$key}:</strong>
        {if is_array($value)}
            <pre>{$value|@print_r}</pre>
        {else}
            {$value}
        {/if}
        <br>
    {/foreach}
{/if}