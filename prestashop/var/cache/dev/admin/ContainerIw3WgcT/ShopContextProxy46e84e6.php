<?php

namespace ContainerIw3WgcT;

class ShopContextProxy46e84e6 extends \PrestaShop\PrestaShop\Core\Context\ShopContext implements \Symfony\Component\VarExporter\LazyObjectInterface
{
    use \Symfony\Component\VarExporter\LazyProxyTrait;

    private const LAZY_OBJECT_PROPERTY_SCOPES = [
        "\0".'*'."\0".'active' => [parent::class, 'active', null, 8],
        "\0".'*'."\0".'associatedShopIds' => [parent::class, 'associatedShopIds', null, 8],
        "\0".'*'."\0".'categoryId' => [parent::class, 'categoryId', null, 8],
        "\0".'*'."\0".'color' => [parent::class, 'color', null, 8],
        "\0".'*'."\0".'domain' => [parent::class, 'domain', null, 8],
        "\0".'*'."\0".'domainSSL' => [parent::class, 'domainSSL', null, 8],
        "\0".'*'."\0".'groupSharingCustomers' => [parent::class, 'groupSharingCustomers', null, 8],
        "\0".'*'."\0".'groupSharingOrders' => [parent::class, 'groupSharingOrders', null, 8],
        "\0".'*'."\0".'groupSharingStocks' => [parent::class, 'groupSharingStocks', null, 8],
        "\0".'*'."\0".'id' => [parent::class, 'id', null, 8],
        "\0".'*'."\0".'isMultiShopEnabled' => [parent::class, 'isMultiShopEnabled', null, 8],
        "\0".'*'."\0".'isMultiShopUsed' => [parent::class, 'isMultiShopUsed', null, 8],
        "\0".'*'."\0".'name' => [parent::class, 'name', null, 8],
        "\0".'*'."\0".'physicalUri' => [parent::class, 'physicalUri', null, 8],
        "\0".'*'."\0".'secured' => [parent::class, 'secured', null, 8],
        "\0".'*'."\0".'shopConstraint' => [parent::class, 'shopConstraint', parent::class, 522],
        "\0".'*'."\0".'shopGroupId' => [parent::class, 'shopGroupId', null, 8],
        "\0".'*'."\0".'themeName' => [parent::class, 'themeName', null, 8],
        "\0".'*'."\0".'virtualUri' => [parent::class, 'virtualUri', null, 8],
        'active' => [parent::class, 'active', null, 8],
        'associatedShopIds' => [parent::class, 'associatedShopIds', null, 8],
        'categoryId' => [parent::class, 'categoryId', null, 8],
        'color' => [parent::class, 'color', null, 8],
        'domain' => [parent::class, 'domain', null, 8],
        'domainSSL' => [parent::class, 'domainSSL', null, 8],
        'groupSharingCustomers' => [parent::class, 'groupSharingCustomers', null, 8],
        'groupSharingOrders' => [parent::class, 'groupSharingOrders', null, 8],
        'groupSharingStocks' => [parent::class, 'groupSharingStocks', null, 8],
        'id' => [parent::class, 'id', null, 8],
        'isMultiShopEnabled' => [parent::class, 'isMultiShopEnabled', null, 8],
        'isMultiShopUsed' => [parent::class, 'isMultiShopUsed', null, 8],
        'name' => [parent::class, 'name', null, 8],
        'physicalUri' => [parent::class, 'physicalUri', null, 8],
        'secured' => [parent::class, 'secured', null, 8],
        'shopConstraint' => [parent::class, 'shopConstraint', parent::class, 522],
        'shopGroupId' => [parent::class, 'shopGroupId', null, 8],
        'themeName' => [parent::class, 'themeName', null, 8],
        'virtualUri' => [parent::class, 'virtualUri', null, 8],
    ];

    public function getShopConstraint(): \PrestaShop\PrestaShop\Core\Domain\Shop\ValueObject\ShopConstraint
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getShopConstraint(...\func_get_args());
        }

        return parent::getShopConstraint(...\func_get_args());
    }

    public function isAllShopContext(): bool
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->isAllShopContext(...\func_get_args());
        }

        return parent::isAllShopContext(...\func_get_args());
    }

    public function isShopGroupContext(): bool
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->isShopGroupContext(...\func_get_args());
        }

        return parent::isShopGroupContext(...\func_get_args());
    }

    public function isSingleShopContext(): bool
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->isSingleShopContext(...\func_get_args());
        }

        return parent::isSingleShopContext(...\func_get_args());
    }

    public function getId(): int
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getId(...\func_get_args());
        }

        return parent::getId(...\func_get_args());
    }

    public function getName(): string
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getName(...\func_get_args());
        }

        return parent::getName(...\func_get_args());
    }

    public function getShopGroupId(): int
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getShopGroupId(...\func_get_args());
        }

        return parent::getShopGroupId(...\func_get_args());
    }

    public function getCategoryId(): int
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getCategoryId(...\func_get_args());
        }

        return parent::getCategoryId(...\func_get_args());
    }

    public function getThemeName(): string
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getThemeName(...\func_get_args());
        }

        return parent::getThemeName(...\func_get_args());
    }

    public function getColor(): string
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getColor(...\func_get_args());
        }

        return parent::getColor(...\func_get_args());
    }

    public function isActive(): bool
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->isActive(...\func_get_args());
        }

        return parent::isActive(...\func_get_args());
    }

    public function getPhysicalUri(): string
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getPhysicalUri(...\func_get_args());
        }

        return parent::getPhysicalUri(...\func_get_args());
    }

    public function getVirtualUri(): string
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getVirtualUri(...\func_get_args());
        }

        return parent::getVirtualUri(...\func_get_args());
    }

    public function getDomain(): string
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getDomain(...\func_get_args());
        }

        return parent::getDomain(...\func_get_args());
    }

    public function getDomainSSL(): string
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getDomainSSL(...\func_get_args());
        }

        return parent::getDomainSSL(...\func_get_args());
    }

    public function getBaseURI(): string
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getBaseURI(...\func_get_args());
        }

        return parent::getBaseURI(...\func_get_args());
    }

    public function getBaseURL(): string
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getBaseURL(...\func_get_args());
        }

        return parent::getBaseURL(...\func_get_args());
    }

    public function hasGroupSharingStocks(): bool
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->hasGroupSharingStocks(...\func_get_args());
        }

        return parent::hasGroupSharingStocks(...\func_get_args());
    }

    public function hasGroupSharingCustomers(): bool
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->hasGroupSharingCustomers(...\func_get_args());
        }

        return parent::hasGroupSharingCustomers(...\func_get_args());
    }

    public function hasGroupSharingOrders(): bool
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->hasGroupSharingOrders(...\func_get_args());
        }

        return parent::hasGroupSharingOrders(...\func_get_args());
    }

    public function getAssociatedShopIds(): array
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getAssociatedShopIds(...\func_get_args());
        }

        return parent::getAssociatedShopIds(...\func_get_args());
    }

    public function isMultiShopEnabled(): bool
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->isMultiShopEnabled(...\func_get_args());
        }

        return parent::isMultiShopEnabled(...\func_get_args());
    }

    public function isMultiShopUsed(): bool
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->isMultiShopUsed(...\func_get_args());
        }

        return parent::isMultiShopUsed(...\func_get_args());
    }
}

// Help opcache.preload discover always-needed symbols
class_exists(\Symfony\Component\VarExporter\Internal\Hydrator::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectRegistry::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectState::class);

if (!\class_exists('ShopContextProxy46e84e6', false)) {
    \class_alias(__NAMESPACE__.'\\ShopContextProxy46e84e6', 'ShopContextProxy46e84e6', false);
}
