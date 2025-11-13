<?php

namespace ContainerIw3WgcT;

class ModuleRepositoryGhostE14692f extends \PrestaShop\PrestaShop\Core\Module\ModuleRepository implements \Symfony\Component\VarExporter\LazyObjectInterface
{
    use \Symfony\Component\VarExporter\LazyGhostTrait;

    private const LAZY_OBJECT_PROPERTY_SCOPES = [
        "\0".parent::class."\0".'adminModuleDataProvider' => [parent::class, 'adminModuleDataProvider', null, 16],
        "\0".parent::class."\0".'cacheProvider' => [parent::class, 'cacheProvider', null, 16],
        "\0".parent::class."\0".'hookManager' => [parent::class, 'hookManager', null, 16],
        "\0".parent::class."\0".'installedModules' => [parent::class, 'installedModules', null, 16],
        "\0".parent::class."\0".'languageContext' => [parent::class, 'languageContext', null, 16],
        "\0".parent::class."\0".'moduleDataProvider' => [parent::class, 'moduleDataProvider', null, 16],
        "\0".parent::class."\0".'modulePath' => [parent::class, 'modulePath', null, 16],
        "\0".parent::class."\0".'modulesFromHook' => [parent::class, 'modulesFromHook', null, 16],
        'adminModuleDataProvider' => [parent::class, 'adminModuleDataProvider', null, 16],
        'cacheProvider' => [parent::class, 'cacheProvider', null, 16],
        'hookManager' => [parent::class, 'hookManager', null, 16],
        'installedModules' => [parent::class, 'installedModules', null, 16],
        'languageContext' => [parent::class, 'languageContext', null, 16],
        'moduleDataProvider' => [parent::class, 'moduleDataProvider', null, 16],
        'modulePath' => [parent::class, 'modulePath', null, 16],
        'modulesFromHook' => [parent::class, 'modulesFromHook', null, 16],
    ];
}

// Help opcache.preload discover always-needed symbols
class_exists(\Symfony\Component\VarExporter\Internal\Hydrator::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectRegistry::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectState::class);

if (!\class_exists('ModuleRepositoryGhostE14692f', false)) {
    \class_alias(__NAMESPACE__.'\\ModuleRepositoryGhostE14692f', 'ModuleRepositoryGhostE14692f', false);
}
