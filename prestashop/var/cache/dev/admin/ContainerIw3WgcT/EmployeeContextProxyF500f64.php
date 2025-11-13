<?php

namespace ContainerIw3WgcT;

class EmployeeContextProxyF500f64 extends \PrestaShop\PrestaShop\Core\Context\EmployeeContext implements \Symfony\Component\VarExporter\LazyObjectInterface
{
    use \Symfony\Component\VarExporter\LazyProxyTrait;

    private const LAZY_OBJECT_PROPERTY_SCOPES = [
        "\0".'*'."\0".'allShopsIds' => [parent::class, 'allShopsIds', parent::class, 522],
        "\0".'*'."\0".'employee' => [parent::class, 'employee', parent::class, 522],
        'allShopsIds' => [parent::class, 'allShopsIds', parent::class, 522],
        'employee' => [parent::class, 'employee', parent::class, 522],
    ];

    public function getEmployee(): ?\PrestaShop\PrestaShop\Core\Context\Employee
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getEmployee(...\func_get_args());
        }

        return parent::getEmployee(...\func_get_args());
    }

    public function hasAuthorizationOnShopGroup(int $shopGroupId): bool
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->hasAuthorizationOnShopGroup(...\func_get_args());
        }

        return parent::hasAuthorizationOnShopGroup(...\func_get_args());
    }

    public function hasAuthorizationOnShop(int $shopId): bool
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->hasAuthorizationOnShop(...\func_get_args());
        }

        return parent::hasAuthorizationOnShop(...\func_get_args());
    }

    public function hasAuthorizationForAllShops(): bool
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->hasAuthorizationForAllShops(...\func_get_args());
        }

        return parent::hasAuthorizationForAllShops(...\func_get_args());
    }

    public function getDefaultShopId(): int
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getDefaultShopId(...\func_get_args());
        }

        return parent::getDefaultShopId(...\func_get_args());
    }

    public function isSuperAdmin(): bool
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->isSuperAdmin(...\func_get_args());
        }

        return parent::isSuperAdmin(...\func_get_args());
    }
}

// Help opcache.preload discover always-needed symbols
class_exists(\Symfony\Component\VarExporter\Internal\Hydrator::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectRegistry::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectState::class);

if (!\class_exists('EmployeeContextProxyF500f64', false)) {
    \class_alias(__NAMESPACE__.'\\EmployeeContextProxyF500f64', 'EmployeeContextProxyF500f64', false);
}
