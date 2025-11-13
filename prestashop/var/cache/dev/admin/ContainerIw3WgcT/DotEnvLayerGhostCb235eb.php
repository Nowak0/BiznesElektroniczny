<?php

namespace ContainerIw3WgcT;

class DotEnvLayerGhostCb235eb extends \PrestaShop\PrestaShop\Core\FeatureFlag\Layer\DotEnvLayer implements \Symfony\Component\VarExporter\LazyObjectInterface
{
    use \Symfony\Component\VarExporter\LazyGhostTrait;

    private const LAZY_OBJECT_PROPERTY_SCOPES = [
        "\0".parent::class."\0".'environment' => [parent::class, 'environment', null, 16],
        "\0".parent::class."\0".'rootDir' => [parent::class, 'rootDir', null, 16],
        'environment' => [parent::class, 'environment', null, 16],
        'rootDir' => [parent::class, 'rootDir', null, 16],
    ];
}

// Help opcache.preload discover always-needed symbols
class_exists(\Symfony\Component\VarExporter\Internal\Hydrator::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectRegistry::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectState::class);

if (!\class_exists('DotEnvLayerGhostCb235eb', false)) {
    \class_alias(__NAMESPACE__.'\\DotEnvLayerGhostCb235eb', 'DotEnvLayerGhostCb235eb', false);
}
