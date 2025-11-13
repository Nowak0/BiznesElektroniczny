<?php

namespace ContainerIw3WgcT;

class EnvLayerGhost89dc26f extends \PrestaShop\PrestaShop\Core\FeatureFlag\Layer\EnvLayer implements \Symfony\Component\VarExporter\LazyObjectInterface
{
    use \Symfony\Component\VarExporter\LazyGhostTrait;

    private const LAZY_OBJECT_PROPERTY_SCOPES = [];
}

// Help opcache.preload discover always-needed symbols
class_exists(\Symfony\Component\VarExporter\Internal\Hydrator::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectRegistry::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectState::class);

if (!\class_exists('EnvLayerGhost89dc26f', false)) {
    \class_alias(__NAMESPACE__.'\\EnvLayerGhost89dc26f', 'EnvLayerGhost89dc26f', false);
}
