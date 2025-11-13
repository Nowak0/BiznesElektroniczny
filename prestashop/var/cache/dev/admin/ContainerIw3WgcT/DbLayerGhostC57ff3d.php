<?php

namespace ContainerIw3WgcT;

class DbLayerGhostC57ff3d extends \PrestaShop\PrestaShop\Core\FeatureFlag\Layer\DbLayer implements \Symfony\Component\VarExporter\LazyObjectInterface
{
    use \Symfony\Component\VarExporter\LazyGhostTrait;

    private const LAZY_OBJECT_PROPERTY_SCOPES = [
        "\0".'*'."\0".'featureFlagRepository' => [parent::class, 'featureFlagRepository', parent::class, 522],
        'featureFlagRepository' => [parent::class, 'featureFlagRepository', parent::class, 522],
    ];
}

// Help opcache.preload discover always-needed symbols
class_exists(\Symfony\Component\VarExporter\Internal\Hydrator::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectRegistry::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectState::class);

if (!\class_exists('DbLayerGhostC57ff3d', false)) {
    \class_alias(__NAMESPACE__.'\\DbLayerGhostC57ff3d', 'DbLayerGhostC57ff3d', false);
}
