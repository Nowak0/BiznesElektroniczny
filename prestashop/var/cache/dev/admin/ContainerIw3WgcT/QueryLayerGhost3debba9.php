<?php

namespace ContainerIw3WgcT;

class QueryLayerGhost3debba9 extends \PrestaShop\PrestaShop\Core\FeatureFlag\Layer\QueryLayer implements \Symfony\Component\VarExporter\LazyObjectInterface
{
    use \Symfony\Component\VarExporter\LazyGhostTrait;

    private const LAZY_OBJECT_PROPERTY_SCOPES = [
        "\0".parent::class."\0".'environment' => [parent::class, 'environment', null, 16],
        "\0".parent::class."\0".'requestStack' => [parent::class, 'requestStack', null, 16],
        'environment' => [parent::class, 'environment', null, 16],
        'requestStack' => [parent::class, 'requestStack', null, 16],
    ];
}

// Help opcache.preload discover always-needed symbols
class_exists(\Symfony\Component\VarExporter\Internal\Hydrator::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectRegistry::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectState::class);

if (!\class_exists('QueryLayerGhost3debba9', false)) {
    \class_alias(__NAMESPACE__.'\\QueryLayerGhost3debba9', 'QueryLayerGhost3debba9', false);
}
