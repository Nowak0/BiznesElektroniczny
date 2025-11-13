<?php

namespace ContainerIw3WgcT;

class ThemeManagerProxy9e13664 extends \PrestaShop\PrestaShop\Core\Addon\Theme\ThemeManager implements \Symfony\Component\VarExporter\LazyObjectInterface
{
    use \Symfony\Component\VarExporter\LazyProxyTrait;

    private const LAZY_OBJECT_PROPERTY_SCOPES = [
        "\0".parent::class."\0".'apiClientContext' => [parent::class, 'apiClientContext', null, 530],
        "\0".parent::class."\0".'configuration' => [parent::class, 'configuration', null, 530],
        "\0".parent::class."\0".'employee' => [parent::class, 'employee', null, 530],
        "\0".parent::class."\0".'filesystem' => [parent::class, 'filesystem', null, 530],
        "\0".parent::class."\0".'finder' => [parent::class, 'finder', null, 16],
        "\0".parent::class."\0".'hookConfigurator' => [parent::class, 'hookConfigurator', null, 530],
        "\0".parent::class."\0".'imageTypeRepository' => [parent::class, 'imageTypeRepository', null, 530],
        "\0".parent::class."\0".'logger' => [parent::class, 'logger', null, 530],
        "\0".parent::class."\0".'shop' => [parent::class, 'shop', null, 16],
        "\0".parent::class."\0".'themeRepository' => [parent::class, 'themeRepository', null, 530],
        "\0".parent::class."\0".'themeValidator' => [parent::class, 'themeValidator', null, 530],
        "\0".parent::class."\0".'translationFinder' => [parent::class, 'translationFinder', null, 530],
        "\0".parent::class."\0".'translator' => [parent::class, 'translator', null, 530],
        'apiClientContext' => [parent::class, 'apiClientContext', null, 530],
        'configuration' => [parent::class, 'configuration', null, 530],
        'employee' => [parent::class, 'employee', null, 530],
        'filesystem' => [parent::class, 'filesystem', null, 530],
        'finder' => [parent::class, 'finder', null, 16],
        'hookConfigurator' => [parent::class, 'hookConfigurator', null, 530],
        'imageTypeRepository' => [parent::class, 'imageTypeRepository', null, 530],
        'logger' => [parent::class, 'logger', null, 530],
        'sandbox' => [parent::class, 'sandbox', null, 4],
        'shop' => [parent::class, 'shop', null, 16],
        'themeRepository' => [parent::class, 'themeRepository', null, 530],
        'themeValidator' => [parent::class, 'themeValidator', null, 530],
        'translationFinder' => [parent::class, 'translationFinder', null, 530],
        'translator' => [parent::class, 'translator', null, 530],
    ];
}

// Help opcache.preload discover always-needed symbols
class_exists(\Symfony\Component\VarExporter\Internal\Hydrator::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectRegistry::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectState::class);

if (!\class_exists('ThemeManagerProxy9e13664', false)) {
    \class_alias(__NAMESPACE__.'\\ThemeManagerProxy9e13664', 'ThemeManagerProxy9e13664', false);
}
