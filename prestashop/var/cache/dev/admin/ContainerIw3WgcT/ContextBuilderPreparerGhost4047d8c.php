<?php

namespace ContainerIw3WgcT;

class ContextBuilderPreparerGhost4047d8c extends \PrestaShop\PrestaShop\Core\Context\ContextBuilderPreparer implements \Symfony\Component\VarExporter\LazyObjectInterface
{
    use \Symfony\Component\VarExporter\LazyGhostTrait;

    private const LAZY_OBJECT_PROPERTY_SCOPES = [
        "\0".parent::class."\0".'languageContextBuilder' => [parent::class, 'languageContextBuilder', null, 530],
        'languageContextBuilder' => [parent::class, 'languageContextBuilder', null, 530],
    ];
}

// Help opcache.preload discover always-needed symbols
class_exists(\Symfony\Component\VarExporter\Internal\Hydrator::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectRegistry::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectState::class);

if (!\class_exists('ContextBuilderPreparerGhost4047d8c', false)) {
    \class_alias(__NAMESPACE__.'\\ContextBuilderPreparerGhost4047d8c', 'ContextBuilderPreparerGhost4047d8c', false);
}
