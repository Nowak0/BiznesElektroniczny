<?php

namespace ContainerIw3WgcT;

class LangRepositoryProxy062aa5d extends \PrestaShopBundle\Entity\Repository\LangRepository implements \Symfony\Component\VarExporter\LazyObjectInterface
{
    use \Symfony\Component\VarExporter\LazyProxyTrait;

    private const LAZY_OBJECT_PROPERTY_SCOPES = [
        "\0".'*'."\0".'_class' => [parent::class, '_class', null, 8],
        "\0".'*'."\0".'_em' => [parent::class, '_em', null, 8],
        "\0".'*'."\0".'_entityName' => [parent::class, '_entityName', null, 8],
        "\0".parent::class."\0".'matches' => [parent::class, 'matches', null, 16],
        '_class' => [parent::class, '_class', null, 8],
        '_em' => [parent::class, '_em', null, 8],
        '_entityName' => [parent::class, '_entityName', null, 8],
        'matches' => [parent::class, 'matches', null, 16],
    ];

    public function getMapping(): array
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getMapping(...\func_get_args());
        }

        return parent::getMapping(...\func_get_args());
    }
}

// Help opcache.preload discover always-needed symbols
class_exists(\Symfony\Component\VarExporter\Internal\Hydrator::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectRegistry::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectState::class);

if (!\class_exists('LangRepositoryProxy062aa5d', false)) {
    \class_alias(__NAMESPACE__.'\\LangRepositoryProxy062aa5d', 'LangRepositoryProxy062aa5d', false);
}
