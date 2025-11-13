<?php

namespace ContainerIw3WgcT;

class FeatureFlagRepositoryProxy035c676 extends \PrestaShopBundle\Entity\Repository\FeatureFlagRepository implements \Symfony\Component\VarExporter\LazyObjectInterface
{
    use \Symfony\Component\VarExporter\LazyProxyTrait;

    private const LAZY_OBJECT_PROPERTY_SCOPES = [
        "\0".'*'."\0".'_class' => [parent::class, '_class', null, 8],
        "\0".'*'."\0".'_em' => [parent::class, '_em', null, 8],
        "\0".'*'."\0".'_entityName' => [parent::class, '_entityName', null, 8],
        '_class' => [parent::class, '_class', null, 8],
        '_em' => [parent::class, '_em', null, 8],
        '_entityName' => [parent::class, '_entityName', null, 8],
    ];

    public function getByName(string $featureFlagName): ?\PrestaShopBundle\Entity\FeatureFlag
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getByName(...\func_get_args());
        }

        return parent::getByName(...\func_get_args());
    }

    public function isEnabled(string $featureFlagName): bool
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->isEnabled(...\func_get_args());
        }

        return parent::isEnabled(...\func_get_args());
    }

    public function isDisabled(string $featureFlagName): bool
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->isDisabled(...\func_get_args());
        }

        return parent::isDisabled(...\func_get_args());
    }

    public function enable(string $featureFlagName): void
    {
        if (isset($this->lazyObjectState)) {
            ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->enable(...\func_get_args());
        } else {
            parent::enable(...\func_get_args());
        }
    }

    public function disable(string $featureFlagName): void
    {
        if (isset($this->lazyObjectState)) {
            ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->disable(...\func_get_args());
        } else {
            parent::disable(...\func_get_args());
        }
    }
}

// Help opcache.preload discover always-needed symbols
class_exists(\Symfony\Component\VarExporter\Internal\Hydrator::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectRegistry::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectState::class);

if (!\class_exists('FeatureFlagRepositoryProxy035c676', false)) {
    \class_alias(__NAMESPACE__.'\\FeatureFlagRepositoryProxy035c676', 'FeatureFlagRepositoryProxy035c676', false);
}
