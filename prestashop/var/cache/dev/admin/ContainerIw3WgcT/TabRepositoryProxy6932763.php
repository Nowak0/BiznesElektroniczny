<?php

namespace ContainerIw3WgcT;

class TabRepositoryProxy6932763 extends \PrestaShopBundle\Entity\Repository\TabRepository implements \Symfony\Component\VarExporter\LazyObjectInterface
{
    use \Symfony\Component\VarExporter\LazyProxyTrait;

    private const LAZY_OBJECT_PROPERTY_SCOPES = [
        "\0".'*'."\0".'_class' => [parent::class, '_class', null, 8],
        "\0".'*'."\0".'_em' => [parent::class, '_em', null, 8],
        "\0".'*'."\0".'_entityName' => [parent::class, '_entityName', null, 8],
        "\0".parent::class."\0".'cachedTabIds' => [parent::class, 'cachedTabIds', null, 16],
        '_class' => [parent::class, '_class', null, 8],
        '_em' => [parent::class, '_em', null, 8],
        '_entityName' => [parent::class, '_entityName', null, 8],
        'cachedTabIds' => [parent::class, 'cachedTabIds', null, 16],
    ];

    public function findOneByRouteName(string $routeName): ?\PrestaShopBundle\Entity\Tab
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->findOneByRouteName(...\func_get_args());
        }

        return parent::findOneByRouteName(...\func_get_args());
    }

    public function getIdByClassName(string $className): int
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getIdByClassName(...\func_get_args());
        }

        return parent::getIdByClassName(...\func_get_args());
    }

    public function getAncestors(int $tabId): array
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getAncestors(...\func_get_args());
        }

        return parent::getAncestors(...\func_get_args());
    }
}

// Help opcache.preload discover always-needed symbols
class_exists(\Symfony\Component\VarExporter\Internal\Hydrator::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectRegistry::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectState::class);

if (!\class_exists('TabRepositoryProxy6932763', false)) {
    \class_alias(__NAMESPACE__.'\\TabRepositoryProxy6932763', 'TabRepositoryProxy6932763', false);
}
