<?php

namespace ContainerIw3WgcT;

class ThemePageLayoutsCustomizerGhost9e9cb9a extends \PrestaShop\PrestaShop\Core\Addon\Theme\ThemePageLayoutsCustomizer implements \Symfony\Component\VarExporter\LazyObjectInterface
{
    use \Symfony\Component\VarExporter\LazyGhostTrait;

    private const LAZY_OBJECT_PROPERTY_SCOPES = [
        "\0".parent::class."\0".'smartyCacheClearer' => [parent::class, 'smartyCacheClearer', null, 16],
        "\0".parent::class."\0".'theme' => [parent::class, 'theme', null, 16],
        "\0".parent::class."\0".'themeManager' => [parent::class, 'themeManager', null, 16],
        'smartyCacheClearer' => [parent::class, 'smartyCacheClearer', null, 16],
        'theme' => [parent::class, 'theme', null, 16],
        'themeManager' => [parent::class, 'themeManager', null, 16],
    ];
}

// Help opcache.preload discover always-needed symbols
class_exists(\Symfony\Component\VarExporter\Internal\Hydrator::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectRegistry::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectState::class);

if (!\class_exists('ThemePageLayoutsCustomizerGhost9e9cb9a', false)) {
    \class_alias(__NAMESPACE__.'\\ThemePageLayoutsCustomizerGhost9e9cb9a', 'ThemePageLayoutsCustomizerGhost9e9cb9a', false);
}
